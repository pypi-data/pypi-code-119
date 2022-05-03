# Copyright (c) 2021 - 2022 TomTom N.V.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# flake8: noqa
# pylint: disable=W0622

"""Init"""

from llvm_diagnostics import formatters

from llvm_diagnostics.messages import (
    Info,
    Warning,
    Error,
    Range,
)

from llvm_diagnostics.utils import Level
from llvm_diagnostics.formatters import config
