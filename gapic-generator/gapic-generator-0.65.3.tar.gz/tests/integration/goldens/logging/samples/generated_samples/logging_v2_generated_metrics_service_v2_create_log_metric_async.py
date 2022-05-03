# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
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
#
# Generated code. DO NOT EDIT!
#
# Snippet for CreateLogMetric
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-logging


# [START logging_v2_generated_MetricsServiceV2_CreateLogMetric_async]
from google.cloud import logging_v2


async def sample_create_log_metric():
    # Create a client
    client = logging_v2.MetricsServiceV2AsyncClient()

    # Initialize request argument(s)
    metric = logging_v2.LogMetric()
    metric.name = "name_value"
    metric.filter = "filter_value"

    request = logging_v2.CreateLogMetricRequest(
        parent="parent_value",
        metric=metric,
    )

    # Make the request
    response = await client.create_log_metric(request=request)

    # Handle the response
    print(response)

# [END logging_v2_generated_MetricsServiceV2_CreateLogMetric_async]
