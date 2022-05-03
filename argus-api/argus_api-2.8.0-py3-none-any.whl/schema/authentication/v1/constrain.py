"""Autogenerated API schema"""
from argus_api import session


constrain = {'tags': ['authentication/v1'], 'summary': 'Request a constrained session (PUBLIC)', 'description': 'This operation will spawn a new user session, where the active userspermissions are constrained to the specified subset of the active users permissions.In addition to returning the constrained session token, the new session will be set as cookies, overwriting any existing session cookies.', 'operationId': 'constrain', 'consumes': ['application/json'], 'produces': ['application/json'], 'parameters': [{'in': 'body', 'name': 'body', 'description': 'Constrain request', 'required': False, 'schema': {'type': 'object', 'properties': {'customer': {'type': 'list', 'position': 0, 'description': 'Set of customers the session should be valid for (default is all current customers). Cannot extend the current set of customers.', 'uniqueItems': True, 'items': {'type': 'string'}}, 'function': {'type': 'list', 'position': 0, 'description': 'Set of functions/roles (by name) the session should be granted (default is all current functions). Cannot extend the current set of functions.', 'uniqueItems': True, 'items': {'type': 'string'}}}}}], 'responses': {'200': {'description': 'successful operation', 'schema': {'required': ['data'], 'properties': {'responseCode': {'type': 'int', 'description': 'Status code returned from API'}, 'limit': {'type': 'int', 'description': 'Maximum number of returned results'}, 'offset': {'type': 'int', 'description': 'Number of skipped results'}, 'count': {'type': 'int', 'description': 'Number of available results on server'}, 'size': {'type': 'int', 'description': 'Actual number of returned results'}, 'metaData': {'type': 'dict', 'description': 'Additional unstructured meta data associated with response'}, 'messages': {'type': 'list', 'description': 'Contains messages returned from the API, usually error messages', 'items': {'type': 'dict', 'properties': {'message': {'type': 'string'}, 'messageTemplate': {'type': 'string'}, 'type': 'str', 'field': {'type': 'string'}, 'parameter': {'type': 'object'}, 'timestamp': {'type': 'int'}, 'options': ['FIELD_ERROR', 'ACTION_ERROR', 'WARNING', 'NOTIFICATION', 'INFO']}}}, 'data': {'type': 'dict', 'properties': {'uri': {'type': 'string'}, 'clientIP': {'type': 'string'}, 'forwardedIP': {'type': 'string'}, 'requestCredentialsType': {'type': 'str', 'enum': ['sessionToken', 'signature', 'apikey']}, 'requestCredentialsData': {'type': 'string'}}}}}}}}