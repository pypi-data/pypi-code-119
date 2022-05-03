"""
TODO
"""


import logging
from pathlib import Path
from typing import Type

from cppython_core.schema import (
    PEP621,
    CPPythonData,
    Generator,
    GeneratorConfiguration,
    GeneratorData,
    GeneratorDataT,
    Interface,
    PyProject,
    TargetEnum,
    ToolData,
)

test_cppython = CPPythonData(**{"target": TargetEnum.EXE})
test_tool = ToolData(cppython=test_cppython)
test_pep621 = PEP621(name="test-project", version="1.0.0", description="This is a test project")
test_pyproject = PyProject(project=test_pep621, tool=test_tool)

test_logger = logging.getLogger(__name__)
test_configuration = GeneratorConfiguration()


class MockInterface(Interface):
    """
    TODO
    """

    def register_logger(self, logger: logging.Logger) -> None:
        """
        TODO
        """

    def read_generator_data(self, generator_data_type: Type[GeneratorDataT]) -> GeneratorDataT:
        """
        TODO
        """
        return generator_data_type()

    def write_pyproject(self) -> None:
        """
        TODO
        """


class MockGenerator(Generator):
    """
    TODO
    """

    def __init__(self, configuration: GeneratorConfiguration, pyproject: PyProject) -> None:
        super().__init__(configuration, pyproject)

        self.downloaded = False

    @staticmethod
    def name() -> str:
        return "test"

    @staticmethod
    def data_type() -> Type[GeneratorData]:
        return GeneratorData

    def generator_downloaded(self, path: Path) -> bool:
        return self.downloaded

    def download_generator(self, path: Path) -> None:
        self.downloaded = True

    def update_generator(self, path: Path) -> None:
        pass

    def install(self) -> None:
        pass

    def update(self) -> None:
        pass

    def build(self) -> None:
        pass
