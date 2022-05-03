"""Autogenerated API schema"""
from argus_api import session


update_instance_status2 = {'tags': ['componentadmin/v2'], 'summary': 'null (INTERNAL)', 'operationId': 'updateInstanceStatus2', 'consumes': ['application/json'], 'produces': ['application/json'], 'parameters': [{'name': 'id', 'in': 'path', 'description': 'ID of instance', 'required': True, 'type': 'int', 'minimum': 1}, {'in': 'body', 'name': 'body', 'description': 'Status update request', 'required': False, 'schema': {'type': 'object', 'required': ['components', 'identifiers', 'state'], 'properties': {'containerID': {'type': 'str', 'position': 0, 'description': 'ID of the currently running container'}, 'identifiers': {'type': 'dict', 'position': 0, 'description': 'Any identifiers for this instance container', 'additionalProperties': {'type': 'string'}}, 'state': {'type': 'str', 'position': 0, 'description': 'The state of this instance container', 'enum': ['initializing', 'started', 'shuttingDown', 'stopped']}, 'components': {'type': 'list', 'position': 0, 'description': 'An optional list of component updates for the root container', 'items': {'type': 'dict', 'required': ['id'], 'properties': {'id': {'type': 'str', 'position': 0, 'description': 'The component UUID'}, 'type': 'str', 'interfaces': {'type': 'list', 'position': 0, 'description': 'Implementing interfaces', 'uniqueItems': True, 'items': {'type': 'string'}}, 'name': {'type': 'str', 'position': 0, 'description': 'The component name'}, 'status': {'type': 'str', 'position': 0, 'description': 'The component status'}}}}, 'instanceID': {'type': 'int', 'position': 0, 'description': 'The instanceID of this container'}, 'runningInstanceRevision': {'type': 'int', 'position': 0, 'description': 'The instance revision of the running container'}, 'runningTemplateRevision': {'type': 'int', 'position': 0, 'description': 'The template revision of the running container'}}}}], 'deprecated': True, 'responses': {'default': {'description': 'successful operation'}}}