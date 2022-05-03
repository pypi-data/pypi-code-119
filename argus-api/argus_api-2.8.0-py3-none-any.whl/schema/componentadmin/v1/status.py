"""Autogenerated API schema"""
from argus_api import session


clear_component_directory = {'tags': ['componentadmin/v1'], 'summary': 'Clear component directory (INTERNAL)', 'description': '', 'operationId': 'clearComponentDirectory', 'produces': ['application/json'], 'parameters': [], 'responses': {'401': {'description': 'Authentication failed'}, '403': {'description': 'Access denied'}}}
get_host_map = {'tags': ['componentadmin/v1'], 'summary': 'Fetch status map (INTERNAL)', 'description': '', 'operationId': 'getHostMap', 'produces': ['application/json'], 'parameters': [], 'responses': {'200': {'description': 'successful operation', 'schema': {'required': ['data'], 'properties': {'responseCode': {'type': 'int', 'description': 'Status code returned from API'}, 'limit': {'type': 'int', 'description': 'Maximum number of returned results'}, 'offset': {'type': 'int', 'description': 'Number of skipped results'}, 'count': {'type': 'int', 'description': 'Number of available results on server'}, 'size': {'type': 'int', 'description': 'Actual number of returned results'}, 'metaData': {'type': 'dict', 'description': 'Additional unstructured meta data associated with response'}, 'messages': {'type': 'list', 'description': 'Contains messages returned from the API, usually error messages', 'items': {'type': 'dict', 'properties': {'message': {'type': 'string'}, 'messageTemplate': {'type': 'string'}, 'type': 'str', 'field': {'type': 'string'}, 'parameter': {'type': 'object'}, 'timestamp': {'type': 'int'}, 'options': ['FIELD_ERROR', 'ACTION_ERROR', 'WARNING', 'NOTIFICATION', 'INFO']}}}, 'data': {'type': 'list', 'description': 'Contains an array of results', 'items': {'type': 'dict', 'properties': {'instances': {'type': 'list', 'items': {'type': 'dict', 'properties': {'installedInstanceRevision': {'type': 'int'}, 'installedTemplateRevision': {'type': 'int'}, 'status': {'type': 'dict', 'properties': {'identity': {'type': 'dict', 'properties': {'exact': {'type': 'boolean'}, 'identifiers': {'type': 'dict', 'additionalProperties': {'type': 'string'}}}}, 'state': {'type': 'str', 'enum': ['NOT_STARTED', 'INITIALIZING', 'STARTED', 'WARNING', 'STOPPING', 'STOPPED', 'FAILED']}}}, 'instanceID': {'type': 'int'}, 'templateID': {'type': 'int'}, 'templateName': {'type': 'string'}, 'monitored': {'type': 'boolean'}, 'inDowntime': {'type': 'boolean'}}}}, 'status': {'type': 'dict', 'properties': {'identity': {'type': 'dict', 'properties': {'exact': {'type': 'boolean'}, 'identifiers': {'type': 'dict', 'additionalProperties': {'type': 'string'}}}}, 'state': {'type': 'str', 'enum': ['NOT_STARTED', 'INITIALIZING', 'STARTED', 'WARNING', 'STOPPING', 'STOPPED', 'FAILED']}}}, 'hostID': {'type': 'int'}, 'monitored': {'type': 'boolean'}, 'inDowntime': {'type': 'boolean'}, 'hostName': {'type': 'string'}}}}}}}, '401': {'description': 'Authentication failed'}, '403': {'description': 'Access denied'}}}
refresh = {'tags': ['componentadmin/v1'], 'summary': 'Request all components to immediately refresh status (INTERNAL)', 'description': '', 'operationId': 'refresh', 'produces': ['application/json'], 'parameters': [], 'responses': {'401': {'description': 'Authentication failed'}, '403': {'description': 'Access denied'}}}