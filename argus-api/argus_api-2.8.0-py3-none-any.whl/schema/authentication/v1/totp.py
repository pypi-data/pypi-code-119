"""Autogenerated API schema"""
from argus_api import session


initialize_totp_generator = {'tags': ['authentication/v1/totp'], 'summary': 'Initiate a new TOTP generator for the user (PUBLIC)', 'description': 'TOTP authentication requires a TOTP generator to be set up for the user.\n\nThis operation allows the user to set up a TOTP generator.\nThis requires TOTP authentication to be enabled for the user.\nThe TOTP initialization request also requires the user to providethe static Argus password for verification.\nThe TOTP generator code retrieved cannot be retrieved again. It should be added directly to the TOTP generator, and should not be stored elsewhere.\n\nAfter initializing, the new TOTP generator is in a pending state, and will notbe active until it is verified using the verification operation.', 'operationId': 'initialize', 'consumes': ['application/json'], 'produces': ['application/json'], 'parameters': [{'in': 'body', 'name': 'body', 'description': 'Initialization request', 'required': False, 'schema': {'type': 'object', 'properties': {'password': {'type': 'str', 'position': 0, 'description': 'User password to verify this request'}, 'authorization': {'type': 'str', 'position': 0, 'description': "User authorization token obtained from the user authorization endpoint. The token must be issued for operation 'totp.initialize'"}}}}], 'responses': {'200': {'description': 'successful operation', 'schema': {'required': ['data'], 'properties': {'responseCode': {'type': 'int', 'description': 'Status code returned from API'}, 'limit': {'type': 'int', 'description': 'Maximum number of returned results'}, 'offset': {'type': 'int', 'description': 'Number of skipped results'}, 'count': {'type': 'int', 'description': 'Number of available results on server'}, 'size': {'type': 'int', 'description': 'Actual number of returned results'}, 'metaData': {'type': 'dict', 'description': 'Additional unstructured meta data associated with response'}, 'messages': {'type': 'list', 'description': 'Contains messages returned from the API, usually error messages', 'items': {'type': 'dict', 'properties': {'message': {'type': 'string'}, 'messageTemplate': {'type': 'string'}, 'type': 'str', 'field': {'type': 'string'}, 'parameter': {'type': 'object'}, 'timestamp': {'type': 'int'}, 'options': ['FIELD_ERROR', 'ACTION_ERROR', 'WARNING', 'NOTIFICATION', 'INFO']}}}, 'data': {'type': 'dict', 'properties': {'userName': {'type': 'string'}, 'passCodeLength': {'type': 'int'}, 'keyAlgorithm': {'type': 'string'}, 'seedBase64': {'type': 'string'}, 'seedBase32': {'type': 'string'}}}}}}, '401': {'description': 'Authentication failed'}, '403': {'description': 'Access denied'}, '404': {'description': 'Not found'}, '412': {'description': 'Validation error'}}}
legacy_totp_authentication = {'tags': ['authentication/v1/totp'], 'summary': 'Initiate a new user session using TOTP authentication (PUBLIC)', 'description': 'Requires TOTP authentication to be enabled on the server, and for the user. \nUse /methods to check which authentication methods are available on the server.\n\nThis is a 2-factor authentication method. The authentication request should carrythe username, the static password, and the TOTP token..\nTokens cannot be reused. Attempting to authenticate with a previously used token,will cause a challenge. Wait for the tokencode to change and resubmit.This endpoint is deprecated, use /totp/authentication instead.', 'operationId': 'legacyTOTPAuthentication', 'consumes': ['application/json'], 'produces': ['application/json'], 'parameters': [{'in': 'body', 'name': 'body', 'description': 'TOTP authentication request', 'required': False, 'schema': {'type': 'object', 'required': ['domain', 'password', 'tokenCode', 'userName'], 'properties': {'requestedAuthorizations': {'type': 'list', 'position': 0, 'description': 'Allow client to request authorizations as part of the authentication transaction. The client is not guaranteed to get the requested authorizations. The setPassword authorization is only returned if the current user has the FORCE_PW_CHANGE flag set.', 'uniqueItems': True, 'items': {'type': 'str', 'enum': ['enrollPublicKey', 'setPassword']}}, 'userName': {'type': 'str', 'position': 0, 'description': 'Username to authenticate'}, 'domain': {'type': 'str', 'position': 0, 'description': 'User domain'}, 'password': {'type': 'str', 'position': 0, 'description': 'Static Argus password'}, 'tokenCode': {'type': 'str', 'position': 0, 'description': 'Current code from TOTP generator'}}}}], 'deprecated': True, 'responses': {'200': {'description': 'successful operation', 'schema': {'required': ['data'], 'properties': {'responseCode': {'type': 'int', 'description': 'Status code returned from API'}, 'limit': {'type': 'int', 'description': 'Maximum number of returned results'}, 'offset': {'type': 'int', 'description': 'Number of skipped results'}, 'count': {'type': 'int', 'description': 'Number of available results on server'}, 'size': {'type': 'int', 'description': 'Actual number of returned results'}, 'metaData': {'type': 'dict', 'description': 'Additional unstructured meta data associated with response'}, 'messages': {'type': 'list', 'description': 'Contains messages returned from the API, usually error messages', 'items': {'type': 'dict', 'properties': {'message': {'type': 'string'}, 'messageTemplate': {'type': 'string'}, 'type': 'str', 'field': {'type': 'string'}, 'parameter': {'type': 'object'}, 'timestamp': {'type': 'int'}, 'options': ['FIELD_ERROR', 'ACTION_ERROR', 'WARNING', 'NOTIFICATION', 'INFO']}}}, 'data': {'type': 'dict', 'properties': {'uri': {'type': 'string'}, 'clientIP': {'type': 'string'}, 'forwardedIP': {'type': 'string'}, 'requestCredentialsType': {'type': 'str', 'enum': ['sessionToken', 'signature', 'apikey']}, 'requestCredentialsData': {'type': 'string'}}}}}}, '401': {'description': 'Authentication failed'}, '206': {'description': 'Authentication challenged', 'schema': {'required': ['data'], 'properties': {'responseCode': {'type': 'integer', 'format': 'int32', 'description': 'Status code returned from API'}, 'limit': {'type': 'integer', 'format': 'int64', 'description': 'Maximum number of returned results'}, 'offset': {'type': 'integer', 'format': 'int64', 'description': 'Number of skipped results'}, 'count': {'type': 'integer', 'format': 'int64', 'description': 'Number of available results on server'}, 'size': {'type': 'integer', 'format': 'int64', 'description': 'Actual number of returned results'}, 'metaData': {'type': 'object', 'description': 'Additional unstructured meta data associated with response'}, 'messages': {'type': 'array', 'description': 'Contains messages returned from the API, usually error messages', 'items': {'type': 'object', 'properties': {'message': {'type': 'string'}, 'messageTemplate': {'type': 'string'}, 'type': {'type': 'string', 'enum': ['FIELD_ERROR', 'ACTION_ERROR', 'WARNING', 'NOTIFICATION', 'INFO']}, 'field': {'type': 'string'}, 'parameter': {'type': 'object'}, 'timestamp': {'type': 'integer', 'format': 'int64'}}}}, 'data': {'type': 'object', 'properties': {'username': {'type': 'string'}, 'failed': {'type': 'boolean'}, 'message': {'type': 'string'}, 'suppressed': {'type': 'array', 'items': {'type': 'object', 'properties': {'cause': {'type': 'object', 'properties': {'cause': [], 'stackTrace': {'type': 'array', 'items': {'type': 'object', 'properties': {'methodName': {'type': 'string'}, 'fileName': {'type': 'string'}, 'lineNumber': {'type': 'integer', 'format': 'int32'}, 'className': {'type': 'string'}, 'nativeMethod': {'type': 'boolean'}}}}, 'message': {'type': 'string'}, 'localizedMessage': {'type': 'string'}, 'suppressed': {'type': 'array', 'items': []}}}, 'stackTrace': {'type': 'array', 'items': {'type': 'object', 'properties': {'methodName': {'type': 'string'}, 'fileName': {'type': 'string'}, 'lineNumber': {'type': 'integer', 'format': 'int32'}, 'className': {'type': 'string'}, 'nativeMethod': {'type': 'boolean'}}}}, 'message': {'type': 'string'}, 'localizedMessage': {'type': 'string'}, 'suppressed': {'type': 'array', 'items': {'type': 'object', 'properties': {'cause': [], 'stackTrace': {'type': 'array', 'items': {'type': 'object', 'properties': {'methodName': {'type': 'string'}, 'fileName': {'type': 'string'}, 'lineNumber': {'type': 'integer', 'format': 'int32'}, 'className': {'type': 'string'}, 'nativeMethod': {'type': 'boolean'}}}}, 'message': {'type': 'string'}, 'localizedMessage': {'type': 'string'}, 'suppressed': {'type': 'array', 'items': []}}}}}}}}}}}}, '221': {'description': 'Session created, password change required', 'schema': {'required': ['data'], 'properties': {'responseCode': {'type': 'integer', 'format': 'int32', 'description': 'Status code returned from API'}, 'limit': {'type': 'integer', 'format': 'int64', 'description': 'Maximum number of returned results'}, 'offset': {'type': 'integer', 'format': 'int64', 'description': 'Number of skipped results'}, 'count': {'type': 'integer', 'format': 'int64', 'description': 'Number of available results on server'}, 'size': {'type': 'integer', 'format': 'int64', 'description': 'Actual number of returned results'}, 'metaData': {'type': 'object', 'description': 'Additional unstructured meta data associated with response'}, 'messages': {'type': 'array', 'description': 'Contains messages returned from the API, usually error messages', 'items': {'type': 'object', 'properties': {'message': {'type': 'string'}, 'messageTemplate': {'type': 'string'}, 'type': {'type': 'string', 'enum': ['FIELD_ERROR', 'ACTION_ERROR', 'WARNING', 'NOTIFICATION', 'INFO']}, 'field': {'type': 'string'}, 'parameter': {'type': 'object'}, 'timestamp': {'type': 'integer', 'format': 'int64'}}}}, 'data': {'type': 'object', 'properties': {'username': {'type': 'string'}, 'cookie': {'type': 'string'}, 'clientIP': {'type': 'string'}, 'forwardedIP': {'type': 'string'}, 'uri': {'type': 'string'}, 'userID': {'type': 'integer', 'format': 'int64'}, 'domainID': {'type': 'integer', 'format': 'int32'}, 'impersonatingUserID': {'type': 'integer', 'format': 'int64'}, 'scope': {'type': 'string', 'enum': ['SESSION', 'REQUEST']}, 'created': {'type': 'integer', 'format': 'int64'}, 'validUntilTimestamp': {'type': 'integer', 'format': 'int64'}, 'securityLevel': {'type': 'string', 'enum': ['ADMINISTRATIVE', 'DEFAULT', 'EXTERNAL']}, 'authenticationMethod': {'type': 'string', 'enum': ['PASSWORD', 'SIGNATURE', 'SMS', 'RADIUS', 'TOTP', 'OTP', 'APIKEY', 'LDAP', 'IMPERSONATED', 'OPENID']}, 'constrained': {'type': 'boolean'}, 'customerConstraints': {'type': 'array', 'uniqueItems': True, 'items': {'type': 'integer', 'format': 'int64'}}, 'functionConstraints': {'type': 'array', 'uniqueItems': True, 'items': {'type': 'integer', 'format': 'int64'}}, 'requestCredentialsData': {'type': 'string'}, 'requestCredentialsType': {'type': 'string', 'enum': ['sessionToken', 'signature', 'apikey']}, 'timestamp': {'type': 'integer', 'format': 'int64'}, 'createdTimestamp': {'type': 'integer', 'format': 'int64'}, 'lastRefreshTimestamp': {'type': 'integer', 'format': 'int64'}, 'sessionKey': {'type': 'string', 'readOnly': True}}}}}}, '412': {'description': 'Validation error'}}}
revoke_totp_generator = {'tags': ['authentication/v1/totp'], 'summary': 'Revoke the current TOTP generator for the user (PUBLIC)', 'description': 'This operation invalidates the current generator config for the user.\nThe user will need to re-initialize the TOTP generator to be able to log inusing TOTP.', 'operationId': 'revoke', 'produces': ['application/json'], 'parameters': [], 'responses': {'200': {'description': 'successful operation', 'schema': {'required': ['data'], 'properties': {'responseCode': {'type': 'int', 'description': 'Status code returned from API'}, 'limit': {'type': 'int', 'description': 'Maximum number of returned results'}, 'offset': {'type': 'int', 'description': 'Number of skipped results'}, 'count': {'type': 'int', 'description': 'Number of available results on server'}, 'size': {'type': 'int', 'description': 'Actual number of returned results'}, 'metaData': {'type': 'dict', 'description': 'Additional unstructured meta data associated with response'}, 'messages': {'type': 'list', 'description': 'Contains messages returned from the API, usually error messages', 'items': {'type': 'dict', 'properties': {'message': {'type': 'string'}, 'messageTemplate': {'type': 'string'}, 'type': 'str', 'field': {'type': 'string'}, 'parameter': {'type': 'object'}, 'timestamp': {'type': 'int'}, 'options': ['FIELD_ERROR', 'ACTION_ERROR', 'WARNING', 'NOTIFICATION', 'INFO']}}}, 'data': {'type': 'object'}}}}, '401': {'description': 'Authentication failed'}, '403': {'description': 'Access denied'}, '404': {'description': 'Not found'}, '412': {'description': 'Validation error'}}}
totp_authentication = {'tags': ['authentication/v1/totp'], 'summary': 'Initiate a new user session using TOTP authentication (PUBLIC)', 'description': 'Requires TOTP authentication to be enabled on the server, and for the user. \nUse /methods to check which authentication methods are available on the server.\n\nThis is a 2-factor authentication method. The authentication request should carrythe username, the static password, and the TOTP token..\nTokens cannot be reused. Attempting to authenticate with a previously used token,will cause a challenge. Wait for the tokencode to change and resubmit.', 'operationId': 'totpAuthentication', 'consumes': ['application/json'], 'produces': ['application/json'], 'parameters': [{'in': 'body', 'name': 'body', 'description': 'TOTP authentication request', 'required': False, 'schema': {'type': 'object', 'required': ['domain', 'password', 'tokenCode', 'userName'], 'properties': {'requestedAuthorizations': {'type': 'list', 'position': 0, 'description': 'Allow client to request authorizations as part of the authentication transaction. The client is not guaranteed to get the requested authorizations. The setPassword authorization is only returned if the current user has the FORCE_PW_CHANGE flag set.', 'uniqueItems': True, 'items': {'type': 'str', 'enum': ['enrollPublicKey', 'setPassword']}}, 'userName': {'type': 'str', 'position': 0, 'description': 'Username to authenticate'}, 'domain': {'type': 'str', 'position': 0, 'description': 'User domain'}, 'password': {'type': 'str', 'position': 0, 'description': 'Static Argus password'}, 'tokenCode': {'type': 'str', 'position': 0, 'description': 'Current code from TOTP generator'}}}}], 'responses': {'200': {'description': 'successful operation', 'schema': {'required': ['data'], 'properties': {'responseCode': {'type': 'int', 'description': 'Status code returned from API'}, 'limit': {'type': 'int', 'description': 'Maximum number of returned results'}, 'offset': {'type': 'int', 'description': 'Number of skipped results'}, 'count': {'type': 'int', 'description': 'Number of available results on server'}, 'size': {'type': 'int', 'description': 'Actual number of returned results'}, 'metaData': {'type': 'dict', 'description': 'Additional unstructured meta data associated with response'}, 'messages': {'type': 'list', 'description': 'Contains messages returned from the API, usually error messages', 'items': {'type': 'dict', 'properties': {'message': {'type': 'string'}, 'messageTemplate': {'type': 'string'}, 'type': 'str', 'field': {'type': 'string'}, 'parameter': {'type': 'object'}, 'timestamp': {'type': 'int'}, 'options': ['FIELD_ERROR', 'ACTION_ERROR', 'WARNING', 'NOTIFICATION', 'INFO']}}}, 'data': {'type': 'dict', 'required': ['credentials', 'sessionKey'], 'properties': {'credentials': {'type': 'dict', 'properties': {'uri': {'type': 'string'}, 'clientIP': {'type': 'string'}, 'forwardedIP': {'type': 'string'}, 'requestCredentialsType': {'type': 'str', 'enum': ['sessionToken', 'signature', 'apikey']}, 'requestCredentialsData': {'type': 'string'}}}, 'sessionKey': {'type': 'str', 'position': 0, 'description': 'The symmetric key created for this session'}, 'authorizations': {'type': 'list', 'position': 0, 'description': 'Any gratuitous authorization tokens generated during authentication, if requested by the client', 'uniqueItems': True, 'items': {'type': 'dict', 'properties': {'operation': {'type': 'str', 'position': 0, 'description': 'Operation which is authorized by this token'}, 'authorization': {'type': 'str', 'position': 0, 'description': 'Authorization JWS string'}, 'nextURI': {'type': 'str', 'position': 0, 'description': 'The URI to proceed to, appending the authorization JWS as a query parameter'}, 'expires': {'type': 'int', 'position': 0, 'description': 'The timestamp when this authorization expires'}}}}}}}}}, '401': {'description': 'Authentication failed'}, '206': {'description': 'Authentication challenged', 'schema': {'required': ['data'], 'properties': {'responseCode': {'type': 'integer', 'format': 'int32', 'description': 'Status code returned from API'}, 'limit': {'type': 'integer', 'format': 'int64', 'description': 'Maximum number of returned results'}, 'offset': {'type': 'integer', 'format': 'int64', 'description': 'Number of skipped results'}, 'count': {'type': 'integer', 'format': 'int64', 'description': 'Number of available results on server'}, 'size': {'type': 'integer', 'format': 'int64', 'description': 'Actual number of returned results'}, 'metaData': {'type': 'object', 'description': 'Additional unstructured meta data associated with response'}, 'messages': {'type': 'array', 'description': 'Contains messages returned from the API, usually error messages', 'items': {'type': 'object', 'properties': {'message': {'type': 'string'}, 'messageTemplate': {'type': 'string'}, 'type': {'type': 'string', 'enum': ['FIELD_ERROR', 'ACTION_ERROR', 'WARNING', 'NOTIFICATION', 'INFO']}, 'field': {'type': 'string'}, 'parameter': {'type': 'object'}, 'timestamp': {'type': 'integer', 'format': 'int64'}}}}, 'data': {'type': 'object', 'properties': {'username': {'type': 'string'}, 'failed': {'type': 'boolean'}, 'message': {'type': 'string'}, 'suppressed': {'type': 'array', 'items': {'type': 'object', 'properties': {'cause': {'type': 'object', 'properties': {'cause': [], 'stackTrace': {'type': 'array', 'items': {'type': 'object', 'properties': {'methodName': {'type': 'string'}, 'fileName': {'type': 'string'}, 'lineNumber': {'type': 'integer', 'format': 'int32'}, 'className': {'type': 'string'}, 'nativeMethod': {'type': 'boolean'}}}}, 'message': {'type': 'string'}, 'localizedMessage': {'type': 'string'}, 'suppressed': {'type': 'array', 'items': []}}}, 'stackTrace': {'type': 'array', 'items': {'type': 'object', 'properties': {'methodName': {'type': 'string'}, 'fileName': {'type': 'string'}, 'lineNumber': {'type': 'integer', 'format': 'int32'}, 'className': {'type': 'string'}, 'nativeMethod': {'type': 'boolean'}}}}, 'message': {'type': 'string'}, 'localizedMessage': {'type': 'string'}, 'suppressed': {'type': 'array', 'items': {'type': 'object', 'properties': {'cause': [], 'stackTrace': {'type': 'array', 'items': {'type': 'object', 'properties': {'methodName': {'type': 'string'}, 'fileName': {'type': 'string'}, 'lineNumber': {'type': 'integer', 'format': 'int32'}, 'className': {'type': 'string'}, 'nativeMethod': {'type': 'boolean'}}}}, 'message': {'type': 'string'}, 'localizedMessage': {'type': 'string'}, 'suppressed': {'type': 'array', 'items': []}}}}}}}}}}}}, '221': {'description': 'Session created, password change required', 'schema': {'required': ['data'], 'properties': {'responseCode': {'type': 'integer', 'format': 'int32', 'description': 'Status code returned from API'}, 'limit': {'type': 'integer', 'format': 'int64', 'description': 'Maximum number of returned results'}, 'offset': {'type': 'integer', 'format': 'int64', 'description': 'Number of skipped results'}, 'count': {'type': 'integer', 'format': 'int64', 'description': 'Number of available results on server'}, 'size': {'type': 'integer', 'format': 'int64', 'description': 'Actual number of returned results'}, 'metaData': {'type': 'object', 'description': 'Additional unstructured meta data associated with response'}, 'messages': {'type': 'array', 'description': 'Contains messages returned from the API, usually error messages', 'items': {'type': 'object', 'properties': {'message': {'type': 'string'}, 'messageTemplate': {'type': 'string'}, 'type': {'type': 'string', 'enum': ['FIELD_ERROR', 'ACTION_ERROR', 'WARNING', 'NOTIFICATION', 'INFO']}, 'field': {'type': 'string'}, 'parameter': {'type': 'object'}, 'timestamp': {'type': 'integer', 'format': 'int64'}}}}, 'data': {'type': 'object', 'properties': {'username': {'type': 'string'}, 'cookie': {'type': 'string'}, 'clientIP': {'type': 'string'}, 'forwardedIP': {'type': 'string'}, 'uri': {'type': 'string'}, 'userID': {'type': 'integer', 'format': 'int64'}, 'domainID': {'type': 'integer', 'format': 'int32'}, 'impersonatingUserID': {'type': 'integer', 'format': 'int64'}, 'scope': {'type': 'string', 'enum': ['SESSION', 'REQUEST']}, 'created': {'type': 'integer', 'format': 'int64'}, 'validUntilTimestamp': {'type': 'integer', 'format': 'int64'}, 'securityLevel': {'type': 'string', 'enum': ['ADMINISTRATIVE', 'DEFAULT', 'EXTERNAL']}, 'authenticationMethod': {'type': 'string', 'enum': ['PASSWORD', 'SIGNATURE', 'SMS', 'RADIUS', 'TOTP', 'OTP', 'APIKEY', 'LDAP', 'IMPERSONATED', 'OPENID']}, 'constrained': {'type': 'boolean'}, 'customerConstraints': {'type': 'array', 'uniqueItems': True, 'items': {'type': 'integer', 'format': 'int64'}}, 'functionConstraints': {'type': 'array', 'uniqueItems': True, 'items': {'type': 'integer', 'format': 'int64'}}, 'requestCredentialsData': {'type': 'string'}, 'requestCredentialsType': {'type': 'string', 'enum': ['sessionToken', 'signature', 'apikey']}, 'timestamp': {'type': 'integer', 'format': 'int64'}, 'createdTimestamp': {'type': 'integer', 'format': 'int64'}, 'lastRefreshTimestamp': {'type': 'integer', 'format': 'int64'}, 'sessionKey': {'type': 'string', 'readOnly': True}}}}}}, '412': {'description': 'Validation error'}}}
totp_user_authorization = {'tags': ['authentication/v1/totp'], 'summary': 'Request an authorization token using TOTP credentials (INTERNAL)', 'description': 'This endpoint requires that the current user is logged in using TOTP authentication. Even if the user has TOTP authentication enabled, it will not work if the current session was creating using a different authentication method.', 'operationId': 'totpUserAuthorization', 'consumes': ['application/json'], 'produces': ['application/json'], 'parameters': [{'in': 'body', 'name': 'body', 'description': 'TOTP authorization request', 'required': False, 'schema': {'type': 'object', 'required': ['nextURI', 'operation', 'tokenCode'], 'properties': {'operation': {'type': 'str', 'position': 0, 'description': 'The name of the operation to authorize'}, 'context': {'type': 'dict', 'position': 0, 'description': 'Context variables to scope this authorization. All context variables required by the executing service must be present and equal to those provided here.', 'additionalProperties': {'type': 'string'}}, 'nextURI': {'type': 'str', 'position': 0, 'description': 'The URI to redirect/route to after successful authorization. The URI will be validated according to policy. The authorization token returned from successful authorization should be appended as a query parameter to this URI.'}, 'tokenCode': {'type': 'str', 'position': 0, 'description': 'The tokencode displayed on the authenticator'}}}}], 'responses': {'200': {'description': 'successful operation', 'schema': {'required': ['data'], 'properties': {'responseCode': {'type': 'int', 'description': 'Status code returned from API'}, 'limit': {'type': 'int', 'description': 'Maximum number of returned results'}, 'offset': {'type': 'int', 'description': 'Number of skipped results'}, 'count': {'type': 'int', 'description': 'Number of available results on server'}, 'size': {'type': 'int', 'description': 'Actual number of returned results'}, 'metaData': {'type': 'dict', 'description': 'Additional unstructured meta data associated with response'}, 'messages': {'type': 'list', 'description': 'Contains messages returned from the API, usually error messages', 'items': {'type': 'dict', 'properties': {'message': {'type': 'string'}, 'messageTemplate': {'type': 'string'}, 'type': 'str', 'field': {'type': 'string'}, 'parameter': {'type': 'object'}, 'timestamp': {'type': 'int'}, 'options': ['FIELD_ERROR', 'ACTION_ERROR', 'WARNING', 'NOTIFICATION', 'INFO']}}}, 'data': {'type': 'dict', 'properties': {'operation': {'type': 'str', 'position': 0, 'description': 'Operation which is authorized by this token'}, 'authorization': {'type': 'str', 'position': 0, 'description': 'Authorization JWS string'}, 'nextURI': {'type': 'str', 'position': 0, 'description': 'The URI to proceed to, appending the authorization JWS as a query parameter'}, 'expires': {'type': 'int', 'position': 0, 'description': 'The timestamp when this authorization expires'}}}}}}, '401': {'description': 'Authentication failed'}, '412': {'description': 'Validation error'}}}
verify_totp_generator = {'tags': ['authentication/v1/totp'], 'summary': 'Verify the pending TOTP generator for the user (PUBLIC)', 'description': 'This operation will activate the pending generator.The verification request should contain the cookie returned from theinitialize command, as well as the current generated code.\n\nIf the user has an existing generator, successfully validatingthe pending generator will invalidate the existing generator.', 'operationId': 'verify', 'consumes': ['application/json'], 'produces': ['application/json'], 'parameters': [{'in': 'body', 'name': 'body', 'description': 'Verification request', 'required': False, 'schema': {'type': 'object', 'required': ['cookie', 'verificationCode'], 'properties': {'cookie': {'type': 'str', 'position': 0, 'description': 'The cookie returned by the TOTP initialization request'}, 'verificationCode': {'type': 'str', 'position': 0, 'description': 'Current code from TOTP generator, to verify correctly generated TOTP code'}}}}], 'responses': {'200': {'description': 'successful operation', 'schema': {'required': ['data'], 'properties': {'responseCode': {'type': 'int', 'description': 'Status code returned from API'}, 'limit': {'type': 'int', 'description': 'Maximum number of returned results'}, 'offset': {'type': 'int', 'description': 'Number of skipped results'}, 'count': {'type': 'int', 'description': 'Number of available results on server'}, 'size': {'type': 'int', 'description': 'Actual number of returned results'}, 'metaData': {'type': 'dict', 'description': 'Additional unstructured meta data associated with response'}, 'messages': {'type': 'list', 'description': 'Contains messages returned from the API, usually error messages', 'items': {'type': 'dict', 'properties': {'message': {'type': 'string'}, 'messageTemplate': {'type': 'string'}, 'type': 'str', 'field': {'type': 'string'}, 'parameter': {'type': 'object'}, 'timestamp': {'type': 'int'}, 'options': ['FIELD_ERROR', 'ACTION_ERROR', 'WARNING', 'NOTIFICATION', 'INFO']}}}, 'data': {'type': 'dict', 'properties': {'message': {'type': 'string'}}}}}}, '401': {'description': 'Authentication failed'}, '403': {'description': 'Access denied'}, '404': {'description': 'Not found'}, '412': {'description': 'Validation error'}}}
#: "initialize" is an alias for "initialize_totp_generator"
initialize = initialize_totp_generator
#: "legacy_t_o_t_p_authentication" is an alias for "legacy_totp_authentication"
legacy_t_o_t_p_authentication = legacy_totp_authentication
#: "revoke" is an alias for "revoke_totp_generator"
revoke = revoke_totp_generator
#: "revoke_5" is an alias for "revoke_totp_generator"
revoke_5 = revoke_totp_generator
#: "verify" is an alias for "verify_totp_generator"
verify = verify_totp_generator