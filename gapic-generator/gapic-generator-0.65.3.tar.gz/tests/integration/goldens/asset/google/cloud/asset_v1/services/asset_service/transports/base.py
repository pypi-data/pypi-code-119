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
import abc
from typing import Awaitable, Callable, Dict, Optional, Sequence, Union
import pkg_resources

import google.auth  # type: ignore
import google.api_core
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.api_core import operations_v1
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account # type: ignore

from google.cloud.asset_v1.types import asset_service
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import empty_pb2  # type: ignore

try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            'google-cloud-asset',
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


class AssetServiceTransport(abc.ABC):
    """Abstract transport class for AssetService."""

    AUTH_SCOPES = (
        'https://www.googleapis.com/auth/cloud-platform',
    )

    DEFAULT_HOST: str = 'cloudasset.googleapis.com'
    def __init__(
            self, *,
            host: str = DEFAULT_HOST,
            credentials: ga_credentials.Credentials = None,
            credentials_file: Optional[str] = None,
            scopes: Optional[Sequence[str]] = None,
            quota_project_id: Optional[str] = None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            always_use_jwt_access: Optional[bool] = False,
            **kwargs,
            ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.
            scopes (Optional[Sequence[str]]): A list of scopes.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
        """

        # Save the hostname. Default to port 443 (HTTPS) if none is specified.
        if ':' not in host:
            host += ':443'
        self._host = host

        scopes_kwargs = {"scopes": scopes, "default_scopes": self.AUTH_SCOPES}

        # Save the scopes.
        self._scopes = scopes

        # If no credentials are provided, then determine the appropriate
        # defaults.
        if credentials and credentials_file:
            raise core_exceptions.DuplicateCredentialArgs("'credentials_file' and 'credentials' are mutually exclusive")

        if credentials_file is not None:
            credentials, _ = google.auth.load_credentials_from_file(
                                credentials_file,
                                **scopes_kwargs,
                                quota_project_id=quota_project_id
                            )
        elif credentials is None:
            credentials, _ = google.auth.default(**scopes_kwargs, quota_project_id=quota_project_id)

        # If the credentials are service account credentials, then always try to use self signed JWT.
        if always_use_jwt_access and isinstance(credentials, service_account.Credentials) and hasattr(service_account.Credentials, "with_always_use_jwt_access"):
            credentials = credentials.with_always_use_jwt_access(True)

        # Save the credentials.
        self._credentials = credentials

    def _prep_wrapped_messages(self, client_info):
        # Precompute the wrapped methods.
        self._wrapped_methods = {
            self.export_assets: gapic_v1.method.wrap_method(
                self.export_assets,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_assets: gapic_v1.method.wrap_method(
                self.list_assets,
                default_timeout=None,
                client_info=client_info,
            ),
            self.batch_get_assets_history: gapic_v1.method.wrap_method(
                self.batch_get_assets_history,
                default_retry=retries.Retry(
initial=0.1,maximum=60.0,multiplier=1.3,                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_feed: gapic_v1.method.wrap_method(
                self.create_feed,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_feed: gapic_v1.method.wrap_method(
                self.get_feed,
                default_retry=retries.Retry(
initial=0.1,maximum=60.0,multiplier=1.3,                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_feeds: gapic_v1.method.wrap_method(
                self.list_feeds,
                default_retry=retries.Retry(
initial=0.1,maximum=60.0,multiplier=1.3,                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_feed: gapic_v1.method.wrap_method(
                self.update_feed,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_feed: gapic_v1.method.wrap_method(
                self.delete_feed,
                default_retry=retries.Retry(
initial=0.1,maximum=60.0,multiplier=1.3,                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.search_all_resources: gapic_v1.method.wrap_method(
                self.search_all_resources,
                default_retry=retries.Retry(
initial=0.1,maximum=60.0,multiplier=1.3,                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=15.0,
                ),
                default_timeout=15.0,
                client_info=client_info,
            ),
            self.search_all_iam_policies: gapic_v1.method.wrap_method(
                self.search_all_iam_policies,
                default_retry=retries.Retry(
initial=0.1,maximum=60.0,multiplier=1.3,                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=15.0,
                ),
                default_timeout=15.0,
                client_info=client_info,
            ),
            self.analyze_iam_policy: gapic_v1.method.wrap_method(
                self.analyze_iam_policy,
                default_retry=retries.Retry(
initial=0.1,maximum=60.0,multiplier=1.3,                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=300.0,
                ),
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.analyze_iam_policy_longrunning: gapic_v1.method.wrap_method(
                self.analyze_iam_policy_longrunning,
                default_timeout=60.0,
                client_info=client_info,
            ),
         }

    def close(self):
        """Closes resources associated with the transport.

       .. warning::
            Only call this method if the transport is NOT shared
            with other clients - this may cause errors in other clients!
        """
        raise NotImplementedError()

    @property
    def operations_client(self):
        """Return the client designed to process long-running operations."""
        raise NotImplementedError()

    @property
    def export_assets(self) -> Callable[
            [asset_service.ExportAssetsRequest],
            Union[
                operations_pb2.Operation,
                Awaitable[operations_pb2.Operation]
            ]]:
        raise NotImplementedError()

    @property
    def list_assets(self) -> Callable[
            [asset_service.ListAssetsRequest],
            Union[
                asset_service.ListAssetsResponse,
                Awaitable[asset_service.ListAssetsResponse]
            ]]:
        raise NotImplementedError()

    @property
    def batch_get_assets_history(self) -> Callable[
            [asset_service.BatchGetAssetsHistoryRequest],
            Union[
                asset_service.BatchGetAssetsHistoryResponse,
                Awaitable[asset_service.BatchGetAssetsHistoryResponse]
            ]]:
        raise NotImplementedError()

    @property
    def create_feed(self) -> Callable[
            [asset_service.CreateFeedRequest],
            Union[
                asset_service.Feed,
                Awaitable[asset_service.Feed]
            ]]:
        raise NotImplementedError()

    @property
    def get_feed(self) -> Callable[
            [asset_service.GetFeedRequest],
            Union[
                asset_service.Feed,
                Awaitable[asset_service.Feed]
            ]]:
        raise NotImplementedError()

    @property
    def list_feeds(self) -> Callable[
            [asset_service.ListFeedsRequest],
            Union[
                asset_service.ListFeedsResponse,
                Awaitable[asset_service.ListFeedsResponse]
            ]]:
        raise NotImplementedError()

    @property
    def update_feed(self) -> Callable[
            [asset_service.UpdateFeedRequest],
            Union[
                asset_service.Feed,
                Awaitable[asset_service.Feed]
            ]]:
        raise NotImplementedError()

    @property
    def delete_feed(self) -> Callable[
            [asset_service.DeleteFeedRequest],
            Union[
                empty_pb2.Empty,
                Awaitable[empty_pb2.Empty]
            ]]:
        raise NotImplementedError()

    @property
    def search_all_resources(self) -> Callable[
            [asset_service.SearchAllResourcesRequest],
            Union[
                asset_service.SearchAllResourcesResponse,
                Awaitable[asset_service.SearchAllResourcesResponse]
            ]]:
        raise NotImplementedError()

    @property
    def search_all_iam_policies(self) -> Callable[
            [asset_service.SearchAllIamPoliciesRequest],
            Union[
                asset_service.SearchAllIamPoliciesResponse,
                Awaitable[asset_service.SearchAllIamPoliciesResponse]
            ]]:
        raise NotImplementedError()

    @property
    def analyze_iam_policy(self) -> Callable[
            [asset_service.AnalyzeIamPolicyRequest],
            Union[
                asset_service.AnalyzeIamPolicyResponse,
                Awaitable[asset_service.AnalyzeIamPolicyResponse]
            ]]:
        raise NotImplementedError()

    @property
    def analyze_iam_policy_longrunning(self) -> Callable[
            [asset_service.AnalyzeIamPolicyLongrunningRequest],
            Union[
                operations_pb2.Operation,
                Awaitable[operations_pb2.Operation]
            ]]:
        raise NotImplementedError()

    @property
    def kind(self) -> str:
        raise NotImplementedError()


__all__ = (
    'AssetServiceTransport',
)
