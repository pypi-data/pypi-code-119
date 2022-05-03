from typing import Any, Optional

from django import forms
from edc_utils import formatted_datetime, to_utc


class CrfRequisitionFormValidatorMixin:

    """An edc_form_validators.FormValidator mixin.

    Used with a CRF that refers to a requisition or requisitions.

    Call in FormValidator.clean.

    For test 'xxx' expects the field trio of 'requisition' and
    'assay_datetime', 'xxx_panel'

        self.required_if_true(
            self.cleaned_data.get('cd4') is not None,
            field_required='cd4_requisition')
        self.validate_requisition(
            'cd4_requisition', 'cd4_assay_datetime', cd4_panel)

    See also, for example: ambition_form_validators.form_validators.blood_result
    """

    assay_datetime_field = "assay_datetime"
    requisition_field = "requisition"

    def validate_requisition(
        self: Any,
        *panels,
        requisition_field: Optional[str] = None,
        assay_datetime_field: Optional[str] = None,
    ):
        """Validates that the requisition model instance exists
        and assay datetime provided.
        """
        requisition_field = requisition_field or self.requisition_field
        assay_datetime_field = assay_datetime_field or self.assay_datetime_field
        requisition = self.cleaned_data.get(requisition_field)
        if requisition and requisition.panel_object not in panels:
            raise forms.ValidationError(
                {
                    requisition_field: (
                        "Incorrect requisition. Unknown panel. "
                        f"Expected one of {[p.name for p in panels]}. "
                        f"Got {requisition.panel_object.name}"
                    )
                }
            )

        self.required_if_true(requisition, field_required=assay_datetime_field)

        self.validate_assay_datetime(requisition, assay_datetime_field)
        return requisition

    def validate_assay_datetime(
        self: Any, requisition: Any, assay_datetime_field: Optional[str] = None
    ):
        assay_datetime_field = assay_datetime_field or self.assay_datetime_field
        assay_datetime = self.cleaned_data.get(assay_datetime_field)
        if assay_datetime:
            assay_datetime = to_utc(assay_datetime)
            requisition_datetime = to_utc(requisition.requisition_datetime)
            if assay_datetime < requisition_datetime:
                raise forms.ValidationError(
                    {
                        assay_datetime_field: (
                            f"Invalid. Cannot be before date of requisition "
                            f"{formatted_datetime(requisition_datetime)}."
                        )
                    }
                )
