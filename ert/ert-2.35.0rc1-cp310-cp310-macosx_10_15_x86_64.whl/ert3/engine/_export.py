from collections import defaultdict
from typing import Any, Dict, List

import ert
import ert3
from ert_shared.async_utils import get_event_loop


def _prepare_export_parameters(
    workspace: ert3.workspace.Workspace,
    experiment_name: str,
    experiment_run_config: ert3.config.ExperimentRunConfig,
    ensemble_size: int,
) -> Dict[str, List[ert.data.record_data]]:
    inputs = defaultdict(list)
    stage_name = experiment_run_config.ensemble_config.forward_model.stage
    step = experiment_run_config.stages_config.step_from_key(stage_name)
    if not step:
        raise ValueError(f"No step for key {stage_name}")

    linked_inputs = experiment_run_config.get_linked_inputs()

    for input_record in experiment_run_config.ensemble_config.input:
        name = input_record.record
        namespace = input_record.source_namespace
        location = input_record.source_location

        if namespace in (ert3.config.SourceNS.storage, ert3.config.SourceNS.stochastic):
            exp_name = None if namespace == "storage" else experiment_name
            source = location if namespace == "storage" else None
            collection = ert.storage.get_ensemble_record(
                workspace_name=workspace.name,
                record_name=name,
                experiment_name=exp_name,
                source=source,
                ensemble_size=ensemble_size,
            )
            # DO NOT export blob records as inputs
            if collection.record_type == ert.data.RecordType.BYTES:
                continue
            for record in collection.records:
                inputs[name].append(record.data)

        elif namespace == ert3.config.SourceNS.resources:
            linked_input = linked_inputs[ert3.config.SourceNS.resources][name]

            if not linked_input.source_transformation:
                continue

            # DO NOT export blob records as inputs
            if (
                linked_input.source_transformation.type
                == ert.data.TransformationType.BINARY
            ):
                continue

            collection = get_event_loop().run_until_complete(
                workspace.load_resource(linked_input)
            )
            assert len(collection) == ensemble_size
            for record in collection.records:
                inputs[name].append(record.data)
        else:
            raise ValueError(f"Unknown record source {input_record.source}")

    return inputs


def _prepare_export_responses(
    workspace_name: str,
    experiment_name: str,
    ensemble: ert3.config.EnsembleConfig,
    ensemble_size: int,
) -> Dict[str, List[ert.data.record_data]]:
    outputs = defaultdict(list)
    records_url = ert.storage.get_records_url(workspace_name, experiment_name)
    responses = ert.storage.get_experiment_responses(experiment_name=experiment_name)

    for record_name in responses:
        for iens in range(ensemble_size):
            url = f"{records_url}/{record_name}?realization_index={iens}"
            future = ert.storage.load_record(url, ert.data.RecordType.LIST_FLOAT)
            record = get_event_loop().run_until_complete(future)
            outputs[record_name].append(record.data)
    return outputs


def export(
    workspace: ert3.workspace.Workspace,
    experiment_name: str,
    experiment_run_config: ert3.config.ExperimentRunConfig,
) -> None:
    workspace.assert_experiment_exists(experiment_name)

    if experiment_name not in ert.storage.get_experiment_names(
        workspace_name=workspace.name
    ):
        raise ValueError("Cannot export experiment that has not been carried out")

    ensemble_size = ert3.engine.get_ensemble_size(
        experiment_run_config=experiment_run_config
    )

    parameters = _prepare_export_parameters(
        workspace,
        experiment_name,
        experiment_run_config,
        ensemble_size,
    )
    responses = _prepare_export_responses(
        workspace.name,
        experiment_name,
        experiment_run_config.ensemble_config,
        ensemble_size,
    )

    data: List[Dict[str, Dict[str, Any]]] = []
    for iens in range(ensemble_size):
        inputs = {record: data[iens] for record, data in parameters.items()}
        outputs = {record: data[iens] for record, data in responses.items()}
        data.append({"input": inputs, "output": outputs})

    workspace.export_json(experiment_name, data)
