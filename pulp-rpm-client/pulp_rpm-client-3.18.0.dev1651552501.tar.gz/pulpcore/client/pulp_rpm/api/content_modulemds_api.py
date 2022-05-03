# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from pulpcore.client.pulp_rpm.api_client import ApiClient
from pulpcore.client.pulp_rpm.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class ContentModulemdsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create(self, relative_path, name, stream, version, context, arch, artifacts, dependencies, **kwargs):  # noqa: E501
        """Create a modulemd  # noqa: E501

        Trigger an asynchronous task to create content,optionally create new repository version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create(relative_path, name, stream, version, context, arch, artifacts, dependencies, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str relative_path: Path where the artifact is located relative to distributions base_path (required)
        :param str name: Modulemd name. (required)
        :param str stream: Stream name. (required)
        :param str version: Modulemd version. (required)
        :param str context: Modulemd context. (required)
        :param str arch: Modulemd architecture. (required)
        :param object artifacts: Modulemd artifacts. (required)
        :param object dependencies: Modulemd dependencies. (required)
        :param str artifact: Artifact file representing the physical content
        :param file file: An uploaded file that may be turned into the artifact of the content unit.
        :param str repository: A URI of a repository the new content unit should be associated with.
        :param bool static_context: Modulemd static-context flag.
        :param list[str] packages: Modulemd artifacts' packages.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: AsyncOperationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_with_http_info(relative_path, name, stream, version, context, arch, artifacts, dependencies, **kwargs)  # noqa: E501

    def create_with_http_info(self, relative_path, name, stream, version, context, arch, artifacts, dependencies, **kwargs):  # noqa: E501
        """Create a modulemd  # noqa: E501

        Trigger an asynchronous task to create content,optionally create new repository version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_with_http_info(relative_path, name, stream, version, context, arch, artifacts, dependencies, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str relative_path: Path where the artifact is located relative to distributions base_path (required)
        :param str name: Modulemd name. (required)
        :param str stream: Stream name. (required)
        :param str version: Modulemd version. (required)
        :param str context: Modulemd context. (required)
        :param str arch: Modulemd architecture. (required)
        :param object artifacts: Modulemd artifacts. (required)
        :param object dependencies: Modulemd dependencies. (required)
        :param str artifact: Artifact file representing the physical content
        :param file file: An uploaded file that may be turned into the artifact of the content unit.
        :param str repository: A URI of a repository the new content unit should be associated with.
        :param bool static_context: Modulemd static-context flag.
        :param list[str] packages: Modulemd artifacts' packages.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(AsyncOperationResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'relative_path',
            'name',
            'stream',
            'version',
            'context',
            'arch',
            'artifacts',
            'dependencies',
            'artifact',
            'file',
            'repository',
            'static_context',
            'packages'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'relative_path' is set
        if self.api_client.client_side_validation and ('relative_path' not in local_var_params or  # noqa: E501
                                                        local_var_params['relative_path'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `relative_path` when calling `create`")  # noqa: E501
        # verify the required parameter 'name' is set
        if self.api_client.client_side_validation and ('name' not in local_var_params or  # noqa: E501
                                                        local_var_params['name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `name` when calling `create`")  # noqa: E501
        # verify the required parameter 'stream' is set
        if self.api_client.client_side_validation and ('stream' not in local_var_params or  # noqa: E501
                                                        local_var_params['stream'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `stream` when calling `create`")  # noqa: E501
        # verify the required parameter 'version' is set
        if self.api_client.client_side_validation and ('version' not in local_var_params or  # noqa: E501
                                                        local_var_params['version'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `version` when calling `create`")  # noqa: E501
        # verify the required parameter 'context' is set
        if self.api_client.client_side_validation and ('context' not in local_var_params or  # noqa: E501
                                                        local_var_params['context'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `context` when calling `create`")  # noqa: E501
        # verify the required parameter 'arch' is set
        if self.api_client.client_side_validation and ('arch' not in local_var_params or  # noqa: E501
                                                        local_var_params['arch'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `arch` when calling `create`")  # noqa: E501

        if self.api_client.client_side_validation and ('relative_path' in local_var_params and  # noqa: E501
                                                        len(local_var_params['relative_path']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `relative_path` when calling `create`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('name' in local_var_params and  # noqa: E501
                                                        len(local_var_params['name']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `name` when calling `create`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('stream' in local_var_params and  # noqa: E501
                                                        len(local_var_params['stream']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `stream` when calling `create`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('version' in local_var_params and  # noqa: E501
                                                        len(local_var_params['version']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `version` when calling `create`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('context' in local_var_params and  # noqa: E501
                                                        len(local_var_params['context']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `context` when calling `create`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('arch' in local_var_params and  # noqa: E501
                                                        len(local_var_params['arch']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `arch` when calling `create`, length must be greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'artifact' in local_var_params:
            form_params.append(('artifact', local_var_params['artifact']))  # noqa: E501
        if 'relative_path' in local_var_params:
            form_params.append(('relative_path', local_var_params['relative_path']))  # noqa: E501
        if 'file' in local_var_params:
            local_var_files['file'] = local_var_params['file']  # noqa: E501
        if 'repository' in local_var_params:
            form_params.append(('repository', local_var_params['repository']))  # noqa: E501
        if 'name' in local_var_params:
            form_params.append(('name', local_var_params['name']))  # noqa: E501
        if 'stream' in local_var_params:
            form_params.append(('stream', local_var_params['stream']))  # noqa: E501
        if 'version' in local_var_params:
            form_params.append(('version', local_var_params['version']))  # noqa: E501
        if 'static_context' in local_var_params:
            form_params.append(('static_context', local_var_params['static_context']))  # noqa: E501
        if 'context' in local_var_params:
            form_params.append(('context', local_var_params['context']))  # noqa: E501
        if 'arch' in local_var_params:
            form_params.append(('arch', local_var_params['arch']))  # noqa: E501
        if 'artifacts' in local_var_params:
            form_params.append(('artifacts', local_var_params['artifacts']))  # noqa: E501
        if 'dependencies' in local_var_params:
            form_params.append(('dependencies', local_var_params['dependencies']))  # noqa: E501
        if 'packages' in local_var_params:
            form_params.append(('packages', local_var_params['packages']))  # noqa: E501
            collection_formats['packages'] = 'csv'  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '/pulp/api/v3/content/rpm/modulemds/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsyncOperationResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list(self, **kwargs):  # noqa: E501
        """List modulemds  # noqa: E501

        ViewSet for Modulemd.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int limit: Number of results to return per page.
        :param str name: Filter results where name matches value
        :param list[str] name__in: Filter results where name is in a comma-separated list of values
        :param int offset: The initial index from which to return the results.
        :param str ordering: Which field to use when ordering the results.
        :param str repository_version: Repository Version referenced by HREF
        :param str repository_version_added: Repository Version referenced by HREF
        :param str repository_version_removed: Repository Version referenced by HREF
        :param str sha256:
        :param str stream: Filter results where stream matches value
        :param list[str] stream__in: Filter results where stream is in a comma-separated list of values
        :param str fields: A list of fields to include in the response.
        :param str exclude_fields: A list of fields to exclude from the response.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PaginatedrpmModulemdResponseList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_with_http_info(**kwargs)  # noqa: E501

    def list_with_http_info(self, **kwargs):  # noqa: E501
        """List modulemds  # noqa: E501

        ViewSet for Modulemd.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int limit: Number of results to return per page.
        :param str name: Filter results where name matches value
        :param list[str] name__in: Filter results where name is in a comma-separated list of values
        :param int offset: The initial index from which to return the results.
        :param str ordering: Which field to use when ordering the results.
        :param str repository_version: Repository Version referenced by HREF
        :param str repository_version_added: Repository Version referenced by HREF
        :param str repository_version_removed: Repository Version referenced by HREF
        :param str sha256:
        :param str stream: Filter results where stream matches value
        :param list[str] stream__in: Filter results where stream is in a comma-separated list of values
        :param str fields: A list of fields to include in the response.
        :param str exclude_fields: A list of fields to exclude from the response.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PaginatedrpmModulemdResponseList, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'limit',
            'name',
            'name__in',
            'offset',
            'ordering',
            'repository_version',
            'repository_version_added',
            'repository_version_removed',
            'sha256',
            'stream',
            'stream__in',
            'fields',
            'exclude_fields'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'name' in local_var_params and local_var_params['name'] is not None:  # noqa: E501
            query_params.append(('name', local_var_params['name']))  # noqa: E501
        if 'name__in' in local_var_params and local_var_params['name__in'] is not None:  # noqa: E501
            query_params.append(('name__in', local_var_params['name__in']))  # noqa: E501
            collection_formats['name__in'] = 'csv'  # noqa: E501
        if 'offset' in local_var_params and local_var_params['offset'] is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
        if 'ordering' in local_var_params and local_var_params['ordering'] is not None:  # noqa: E501
            query_params.append(('ordering', local_var_params['ordering']))  # noqa: E501
        if 'repository_version' in local_var_params and local_var_params['repository_version'] is not None:  # noqa: E501
            query_params.append(('repository_version', local_var_params['repository_version']))  # noqa: E501
        if 'repository_version_added' in local_var_params and local_var_params['repository_version_added'] is not None:  # noqa: E501
            query_params.append(('repository_version_added', local_var_params['repository_version_added']))  # noqa: E501
        if 'repository_version_removed' in local_var_params and local_var_params['repository_version_removed'] is not None:  # noqa: E501
            query_params.append(('repository_version_removed', local_var_params['repository_version_removed']))  # noqa: E501
        if 'sha256' in local_var_params and local_var_params['sha256'] is not None:  # noqa: E501
            query_params.append(('sha256', local_var_params['sha256']))  # noqa: E501
        if 'stream' in local_var_params and local_var_params['stream'] is not None:  # noqa: E501
            query_params.append(('stream', local_var_params['stream']))  # noqa: E501
        if 'stream__in' in local_var_params and local_var_params['stream__in'] is not None:  # noqa: E501
            query_params.append(('stream__in', local_var_params['stream__in']))  # noqa: E501
            collection_formats['stream__in'] = 'csv'  # noqa: E501
        if 'fields' in local_var_params and local_var_params['fields'] is not None:  # noqa: E501
            query_params.append(('fields', local_var_params['fields']))  # noqa: E501
        if 'exclude_fields' in local_var_params and local_var_params['exclude_fields'] is not None:  # noqa: E501
            query_params.append(('exclude_fields', local_var_params['exclude_fields']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '/pulp/api/v3/content/rpm/modulemds/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PaginatedrpmModulemdResponseList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def read(self, rpm_modulemd_href, **kwargs):  # noqa: E501
        """Inspect a modulemd  # noqa: E501

        ViewSet for Modulemd.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read(rpm_modulemd_href, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str rpm_modulemd_href: (required)
        :param str fields: A list of fields to include in the response.
        :param str exclude_fields: A list of fields to exclude from the response.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: RpmModulemdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.read_with_http_info(rpm_modulemd_href, **kwargs)  # noqa: E501

    def read_with_http_info(self, rpm_modulemd_href, **kwargs):  # noqa: E501
        """Inspect a modulemd  # noqa: E501

        ViewSet for Modulemd.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_with_http_info(rpm_modulemd_href, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str rpm_modulemd_href: (required)
        :param str fields: A list of fields to include in the response.
        :param str exclude_fields: A list of fields to exclude from the response.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(RpmModulemdResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'rpm_modulemd_href',
            'fields',
            'exclude_fields'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method read" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'rpm_modulemd_href' is set
        if self.api_client.client_side_validation and ('rpm_modulemd_href' not in local_var_params or  # noqa: E501
                                                        local_var_params['rpm_modulemd_href'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `rpm_modulemd_href` when calling `read`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'rpm_modulemd_href' in local_var_params:
            path_params['rpm_modulemd_href'] = local_var_params['rpm_modulemd_href']  # noqa: E501

        query_params = []
        if 'fields' in local_var_params and local_var_params['fields'] is not None:  # noqa: E501
            query_params.append(('fields', local_var_params['fields']))  # noqa: E501
        if 'exclude_fields' in local_var_params and local_var_params['exclude_fields'] is not None:  # noqa: E501
            query_params.append(('exclude_fields', local_var_params['exclude_fields']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '{rpm_modulemd_href}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RpmModulemdResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
