"""Autogenerated API schema"""
from argus_api import session


get_events_for_case = {'tags': ['events/v1'], 'summary': 'Fetch events associated with specified case (PUBLIC)', 'description': 'Fetch events associated with case that has ID specified in the url, it will also figure out which cases have been merged into the specified case,and fetch events for those merged cases as well.\nResult of events will be sorted by event start timestamp in descending order.', 'operationId': 'getEventsForCase', 'produces': ['application/json', 'text/csv'], 'parameters': [{'name': 'caseID', 'in': 'path', 'description': 'Case ID', 'required': True, 'type': 'int', 'minimum': 1}, {'name': 'limit', 'in': 'query', 'description': 'Maximum number of returned results, 0 is everything and will give an error if the result is more than allowed.', 'required': False, 'type': 'int', 'default': 25, 'maximum': 10000, 'minimum': 0}, {'name': 'offset', 'in': 'query', 'description': 'Skip a number of results', 'required': False, 'type': 'int', 'default': 0, 'minimum': 0}, {'name': 'sortBy', 'in': 'query', 'description': 'List of properties to sort by (prefix with "-" to sort descending).Only accepts timestamp and -timestamp.If no value is given, it defaults to sorting by descending timestamp.', 'required': False, 'type': 'list', 'items': {'type': 'string'}, 'collectionFormat': 'multi'}], 'responses': {'200': {'description': 'successful operation', 'schema': {'required': ['data'], 'properties': {'responseCode': {'type': 'int', 'description': 'Status code returned from API'}, 'limit': {'type': 'int', 'description': 'Maximum number of returned results'}, 'offset': {'type': 'int', 'description': 'Number of skipped results'}, 'count': {'type': 'int', 'description': 'Number of available results on server'}, 'size': {'type': 'int', 'description': 'Actual number of returned results'}, 'metaData': {'type': 'dict', 'description': 'Additional unstructured meta data associated with response'}, 'messages': {'type': 'list', 'description': 'Contains messages returned from the API, usually error messages', 'items': {'type': 'dict', 'properties': {'message': {'type': 'string'}, 'messageTemplate': {'type': 'string'}, 'type': 'str', 'field': {'type': 'string'}, 'parameter': {'type': 'object'}, 'timestamp': {'type': 'int'}, 'options': ['FIELD_ERROR', 'ACTION_ERROR', 'WARNING', 'NOTIFICATION', 'INFO']}}}, 'data': {'type': 'list', 'description': 'Contains an array of results', 'items': {'type': 'dict', 'properties': {'customerInfo': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}, 'shortName': {'type': 'string'}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}}}, 'properties': {'type': 'dict', 'additionalProperties': {'type': 'string'}}, 'comments': {'type': 'list', 'items': {'type': 'dict', 'properties': {'timestamp': {'type': 'int', 'position': 0, 'description': 'When the comment was added.'}, 'user': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'customer': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}, 'shortName': {'type': 'string'}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}}}, 'domain': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'name': {'type': 'string'}}}, 'userName': {'type': 'string'}, 'name': {'type': 'string'}, 'customerID': {'type': 'int'}}}, 'comment': {'type': 'str', 'position': 0, 'description': "The comment's text."}}}}, 'associatedCase': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'subject': {'type': 'string'}, 'categoryID': {'type': 'int'}, 'categoryName': {'type': 'string'}, 'service': {'type': 'string'}, 'status': {'type': 'str', 'enum': ['ATTACHMENT_ADDED', 'PENDING_CUSTOMER', 'PENDING_SOC', 'PENDING_VENDOR', 'WORKING_SOC', 'WORKING_CUSTOMER', 'PENDING_CLOSE', 'CLOSED']}, 'priority': {'type': 'str', 'enum': ['low', 'medium', 'high', 'critical']}}}, 'associatedCases': {'type': 'list', 'uniqueItems': True, 'items': {'type': 'dict', 'properties': {'id': {'type': 'int'}, 'subject': {'type': 'string'}, 'categoryID': {'type': 'int'}, 'categoryName': {'type': 'string'}, 'service': {'type': 'string'}, 'status': {'type': 'str', 'enum': ['ATTACHMENT_ADDED', 'PENDING_CUSTOMER', 'PENDING_SOC', 'PENDING_VENDOR', 'WORKING_SOC', 'WORKING_CUSTOMER', 'PENDING_CLOSE', 'CLOSED']}, 'priority': {'type': 'str', 'enum': ['low', 'medium', 'high', 'critical']}}}}, 'location': {'type': 'dict', 'properties': {'shortName': {'type': 'string'}, 'name': {'type': 'string'}, 'timeZone': {'type': 'string'}, 'id': {'type': 'int'}}}, 'attackInfo': {'type': 'dict', 'properties': {'alarmID': {'type': 'int'}, 'alarmDescription': {'type': 'string'}, 'attackCategoryID': {'type': 'int'}, 'attackCategoryName': {'type': 'string'}, 'signature': {'type': 'string'}}}, 'domain': {'type': 'dict', 'properties': {'fqdn': {'type': 'string'}}}, 'uri': {'type': 'string'}, 'count': {'type': 'int'}, 'source': {'type': 'dict', 'properties': {'port': {'type': 'int'}, 'geoLocation': {'type': 'dict', 'properties': {'countryCode': {'type': 'string'}, 'countryName': {'type': 'string'}, 'locationName': {'type': 'string'}, 'latitude': {'type': 'float'}, 'longitude': {'type': 'float'}}}, 'networkAddress': {'type': 'dict', 'properties': {'ipv6': {'type': 'bool', 'xml': {'attribute': True}, 'readOnly': True}, 'maskBits': {'type': 'int'}, 'host': {'type': 'bool', 'xml': {'attribute': True}, 'readOnly': True}, 'multicast': {'type': 'boolean'}, 'public': {'type': 'boolean'}, 'address': {'type': 'str', 'xml': {'attribute': True}, 'readOnly': True}}}}}, 'destination': {'type': 'dict', 'properties': {'port': {'type': 'int'}, 'geoLocation': {'type': 'dict', 'properties': {'countryCode': {'type': 'string'}, 'countryName': {'type': 'string'}, 'locationName': {'type': 'string'}, 'latitude': {'type': 'float'}, 'longitude': {'type': 'float'}}}, 'networkAddress': {'type': 'dict', 'properties': {'ipv6': {'type': 'bool', 'xml': {'attribute': True}, 'readOnly': True}, 'maskBits': {'type': 'int'}, 'host': {'type': 'bool', 'xml': {'attribute': True}, 'readOnly': True}, 'multicast': {'type': 'boolean'}, 'public': {'type': 'boolean'}, 'address': {'type': 'str', 'xml': {'attribute': True}, 'readOnly': True}}}}}, 'protocol': {'type': 'string'}, 'timestamp': {'type': 'int'}, 'startTimestamp': {'type': 'int'}, 'endTimestamp': {'type': 'int'}, 'lastUpdatedTimestamp': {'type': 'int'}, 'flags': {'type': 'list', 'readOnly': True, 'uniqueItems': True, 'items': {'type': 'str', 'enum': ['ESTABLISHED', 'BLOCKED', 'SNAPSHOT', 'FINALIZED', 'SOURCE_IS_CUSTOMERNET', 'DESTINATION_IS_CUSTOMERNET', 'SOURCE_IS_PARTIAL_CUSTOMERNET', 'DESTINATION_IS_PARTIAL_CUSTOMERNET', 'INTRUDER_IS_CUSTOMERNET', 'VICTIM_IS_CUSTOMERNET', 'INTRUDER_IS_PARTIAL_CUSTOMERNET', 'VICTIM_IS_PARTIAL_CUSTOMERNET', 'PARTIALLY_BLOCKED', 'FALSE_POSITIVE', 'NOT_A_THREAT', 'TUNING_CANDIDATE', 'NOTIFIED', 'PARTIALLY_NOTIFIED', 'FOLLOWUP', 'IDENTIFIED_THREAT', 'THREAT_CANDIDATE', 'ACKNOWLEDGED', 'PARTIALLY_ACKNOWLEDGED', 'SEVERITY_ADJUSTED', 'COMMENTED', 'FILTERED', 'CHECKED', 'INCOMPLETE_DETAILS', 'AGGREGATED_BASE_EVENT', 'REMOTE_STORAGE', 'CUSTOM_SOURCE_AGGREGATION', 'CUSTOM_DESTINATION_AGGREGATION', 'CUSTOM_INTRUDER_AGGREGATION', 'CUSTOM_VICTIM_AGGREGATION', 'HAS_PAYLOAD', 'HAS_PCAP', 'ASSOCIATED_TO_CASE_BY_FILTER', 'SEVERITY_INCREASED_BY_FILTER', 'SEVERITY_REDUCED_BY_FILTER', 'CREATED_BY_ANALYSIS_FILTER', 'EXTEND_EVENT_TTL', 'INITIAL_TUNING', 'POST_ANALYSIS', 'PARTIAL_SSL_TERMINATED', 'SSL_TERMINATED', 'AUTO_REPORT', 'MISSING_TIMESTAMP', 'CLOCK_OUT_OF_SYNC', 'DROP_ANALYSIS', 'ESCALATED_BY_REPUTATION', 'HAS_SAMPLE', 'STORE_EVENT', 'STORE_AGGREGATED', 'SOURCE_IS_MANAGED_BY_SOC', 'DESTINATION_IS_MANAGED_BY_SOC']}}, 'severity': {'type': 'str', 'readOnly': True, 'enum': ['low', 'medium', 'high', 'critical']}, 'detailedEventIDS': {'type': 'list', 'readOnly': True, 'uniqueItems': True, 'items': {'type': 'string'}}, 'id': {'type': 'str', 'xml': {'attribute': True}, 'readOnly': True}}}}}}}, '401': {'description': 'Authentication failed'}, '403': {'description': 'Access denied'}, '412': {'description': 'Validation failed'}}}