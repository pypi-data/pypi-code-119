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
# Snippet for SearchAllIamPolicies
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-asset


# [START cloudasset_v1_generated_AssetService_SearchAllIamPolicies_sync]
from google.cloud import asset_v1


def sample_search_all_iam_policies():
    # Create a client
    client = asset_v1.AssetServiceClient()

    # Initialize request argument(s)
    request = asset_v1.SearchAllIamPoliciesRequest(
        scope="scope_value",
    )

    # Make the request
    page_result = client.search_all_iam_policies(request=request)

    # Handle the response
    for response in page_result:
        print(response)

# [END cloudasset_v1_generated_AssetService_SearchAllIamPolicies_sync]
