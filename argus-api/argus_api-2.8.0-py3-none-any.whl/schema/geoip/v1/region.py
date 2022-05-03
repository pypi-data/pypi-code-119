"""Autogenerated API schema"""
from argus_api import session


add_region = {'tags': ['/geoip/v1'], 'summary': 'Add new region (DEV)', 'description': '', 'operationId': 'addRegion', 'consumes': ['application/json'], 'produces': ['application/json'], 'parameters': [{'in': 'body', 'name': 'body', 'required': False, 'schema': {'type': 'object', 'properties': {'id': {'type': 'int'}, 'countryCode': {'type': 'string'}, 'regionCode': {'type': 'string'}, 'regionName': {'type': 'string'}, 'lastModified': {'type': 'int'}, 'flags': {'type': 'int'}, 'minLocationID': {'type': 'int'}, 'maxLocationID': {'type': 'int'}}}}], 'responses': {'201': {'description': 'successful operation', 'schema': {'required': ['data'], 'properties': {'responseCode': {'type': 'int', 'description': 'Status code returned from API'}, 'limit': {'type': 'int', 'description': 'Maximum number of returned results'}, 'offset': {'type': 'int', 'description': 'Number of skipped results'}, 'count': {'type': 'int', 'description': 'Number of available results on server'}, 'size': {'type': 'int', 'description': 'Actual number of returned results'}, 'metaData': {'type': 'dict', 'description': 'Additional unstructured meta data associated with response'}, 'messages': {'type': 'list', 'description': 'Contains messages returned from the API, usually error messages', 'items': {'type': 'dict', 'properties': {'message': {'type': 'string'}, 'messageTemplate': {'type': 'string'}, 'type': 'str', 'field': {'type': 'string'}, 'parameter': {'type': 'object'}, 'timestamp': {'type': 'int'}, 'options': ['FIELD_ERROR', 'ACTION_ERROR', 'WARNING', 'NOTIFICATION', 'INFO']}}}, 'data': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'countryCode': {'type': 'string'}, 'regionCode': {'type': 'string'}, 'regionName': {'type': 'string'}, 'lastModified': {'type': 'int'}, 'flags': {'type': 'int'}, 'minLocationID': {'type': 'int'}, 'maxLocationID': {'type': 'int'}}}}}}, '401': {'description': 'Authentication failed'}, '403': {'description': 'Access denied'}, '412': {'description': 'Validation failed'}}}