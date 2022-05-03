"""Autogenerated API schema"""
from argus_api import session


search_records = {'tags': ['pdns/v3'], 'summary': 'Search against PassiveDNS with criteria and return matching records (PUBLIC)', 'description': 'Search against PassiveDNS with criteria and return matching records. If user exceeds current resource limits, this operation may return status code 402. If that happens, the metaData key millisUntilResourcesAvailable gives a hint as to how long the client needs to wait before attempting again.', 'operationId': 'searchRecords', 'consumes': ['application/json'], 'produces': ['application/json'], 'parameters': [{'in': 'body', 'name': 'body', 'required': False, 'schema': {'type': 'object', 'required': ['query'], 'properties': {'query': {'type': 'str', 'position': 0, 'description': 'Lookup query '}, 'aggregateResult': {'type': 'bool', 'position': 0, 'description': 'Whether aggregate results (default true) '}, 'includeAnonymousResults': {'type': 'bool', 'position': 0, 'description': 'Whether include anonymous results (default true) '}, 'rrClass': {'type': 'list', 'position': 0, 'description': 'Lookup with specified record classes ', 'uniqueItems': True, 'items': {'type': 'string'}}, 'rrType': {'type': 'list', 'position': 0, 'description': 'Lookup with specified record types ', 'uniqueItems': True, 'items': {'type': 'string'}}, 'customerID': {'type': 'list', 'position': 0, 'description': 'Lookup for specified customer IDs ', 'uniqueItems': True, 'items': {'type': 'int'}}, 'tlp': {'type': 'list', 'position': 0, 'description': 'Lookup with specified TLPs, public usage only TLP white allowed ', 'uniqueItems': True, 'items': {'type': 'str', 'enum': ['white', 'green', 'amber', 'red']}}, 'limit': {'type': 'int', 'position': 0, 'description': 'Max number of results to be returned, default unset means default limit 25 will be used, 0 means unlimited '}, 'offset': {'type': 'int', 'position': 0, 'description': 'Number of results to be skipped first, default 0 (default 0)', 'minimum': 0, 'default': 0}}}}], 'responses': {'200': {'description': 'successful operation', 'schema': {'required': ['data'], 'properties': {'responseCode': {'type': 'int', 'description': 'Status code returned from API'}, 'limit': {'type': 'int', 'description': 'Maximum number of returned results'}, 'offset': {'type': 'int', 'description': 'Number of skipped results'}, 'count': {'type': 'int', 'description': 'Number of available results on server'}, 'size': {'type': 'int', 'description': 'Actual number of returned results'}, 'metaData': {'type': 'dict', 'description': 'Additional unstructured meta data associated with response'}, 'messages': {'type': 'list', 'description': 'Contains messages returned from the API, usually error messages', 'items': {'type': 'dict', 'properties': {'message': {'type': 'string'}, 'messageTemplate': {'type': 'string'}, 'type': 'str', 'field': {'type': 'string'}, 'parameter': {'type': 'object'}, 'timestamp': {'type': 'int'}, 'options': ['FIELD_ERROR', 'ACTION_ERROR', 'WARNING', 'NOTIFICATION', 'INFO']}}}, 'data': {'type': 'list', 'description': 'Contains an array of results', 'items': {'type': 'dict', 'properties': {'createdTimestamp': {'type': 'int'}, 'lastUpdatedTimestamp': {'type': 'int'}, 'times': {'type': 'int'}, 'tlp': {'type': 'str', 'enum': ['white', 'green', 'amber', 'red']}, 'query': {'type': 'string'}, 'answer': {'type': 'string'}, 'minTtl': {'type': 'int'}, 'maxTtl': {'type': 'int'}, 'customer': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}, 'shortName': {'type': 'string'}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}}}, 'lastSeenTimestamp': {'type': 'int', 'readOnly': True}, 'firstSeenTimestamp': {'type': 'int', 'readOnly': True}, 'rrclass': {'type': 'str', 'readOnly': True, 'enum': ['in']}, 'rrtype': {'type': 'str', 'readOnly': True, 'enum': ['a', 'aaaa', 'cname', 'dname', 'mx', 'naptr', 'ns', 'ptr', 'rp', 'soa', 'srv', 'txt']}}}}}}}, '401': {'description': 'Authentication failed'}, '402': {'description': 'Resource limit exceeded.'}, '403': {'description': 'Access denied'}, '412': {'description': 'Validation failed'}}}