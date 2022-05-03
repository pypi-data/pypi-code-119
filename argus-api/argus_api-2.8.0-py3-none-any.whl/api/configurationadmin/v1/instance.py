"""Autogenerated API"""
from argus_api import session
import logging
from argus_cli.plugin import register_command
from argus_plugins import argus_cli_module
from argus_api.utils import deprecated_alias
log = logging.getLogger(__name__)


@register_command(
    extending=("configurationadmin", "v1", "instance"),
    module=argus_cli_module
)
def add_instance_comment(
    id: int,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
) -> dict:
    """Add a comment to configuration instance (INTERNAL)
    
    :param int id: ID of instance to comment
    :param json: return the response's body as a ``dict`` parsed from json. ``True`` by
      default. If set to false, the raw ``requests.Response`` object will be returned.
    :param verify: path to a certificate bundle or boolean indicating whether SSL
      verification should be performed.
    :param apiKey: Argus API key.
    :param authentication: authentication override
    :param server_url: API base URL override
    :param body: body of the request. other parameters will override keys defined in the body.
    :raises AuthenticationFailedException: on 401
    :raises AccessDeniedException: on 403
    :raises ObjectNotFoundException: on 404
    :raises ValidationErrorException: on 412
    :raises ArgusException: on other status codes
    
    :returns: dictionary translated from JSON
    """

    route = "/configurationadmin/v1/instance/{id}/comment".format(id=id)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

    query_parameters = {}
    log.debug("POST %s (headers: %s, body: %s)" % (route, str(headers), str(body) or ""))

    response = session.post(
        route,
        params=query_parameters or None,
        data=body or None,
        verify=verify,
        apiKey=apiKey,
        authentication=authentication,
        server_url=server_url,
        headers=headers,
        proxies=proxies,
    )
    return response.json() if json else response

@register_command(
    extending=("configurationadmin", "v1", "instance"),
    module=argus_cli_module
)
def create_instance(
    templateID: int = None,
    hostID: int = None,
    parentID: int = None,
    information: str = None,
    properties: dict = None,
    identifiers: dict = None,
    codeProfile: str = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
) -> dict:
    """Create new configuration instance (INTERNAL)
    
    :param int templateID: 
    :param int hostID: 
    :param int parentID: 
    :param str information: \[\\s\\w\\\{\\\}\\\$\\\-\\\(\\\)\\.\\\[\\\]\"\\\'\_\/\\\\\,\\\*\\\+\\\#\:\@\!\?\;\=\]\*
    :param dict properties: 
    :param dict identifiers: 
    :param str codeProfile: \[a\-zA\-Z0\-9\_\\\-\\.\]\*
    :param json: return the response's body as a ``dict`` parsed from json. ``True`` by
      default. If set to false, the raw ``requests.Response`` object will be returned.
    :param verify: path to a certificate bundle or boolean indicating whether SSL
      verification should be performed.
    :param apiKey: Argus API key.
    :param authentication: authentication override
    :param server_url: API base URL override
    :param body: body of the request. other parameters will override keys defined in the body.
    :raises AuthenticationFailedException: on 401
    :raises AccessDeniedException: on 403
    :raises ValidationErrorException: on 412
    :raises ArgusException: on other status codes
    
    :returns: dictionary translated from JSON
    """

    route = "/configurationadmin/v1/instance".format()

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}
    # Only send templateID if the argument was provided, dont send null values
    if templateID is not None:
        body.update({"templateID": templateID})
    # Only send hostID if the argument was provided, dont send null values
    if hostID is not None:
        body.update({"hostID": hostID})
    # Only send parentID if the argument was provided, dont send null values
    if parentID is not None:
        body.update({"parentID": parentID})
    # Only send information if the argument was provided, dont send null values
    if information is not None:
        body.update({"information": information})
    # Only send properties if the argument was provided, dont send null values
    if properties is not None:
        body.update({"properties": properties})
    # Only send identifiers if the argument was provided, dont send null values
    if identifiers is not None:
        body.update({"identifiers": identifiers})
    # Only send codeProfile if the argument was provided, dont send null values
    if codeProfile is not None:
        body.update({"codeProfile": codeProfile})

    query_parameters = {}
    log.debug("POST %s (headers: %s, body: %s)" % (route, str(headers), str(body) or ""))

    response = session.post(
        route,
        params=query_parameters or None,
        json=body,
        verify=verify,
        apiKey=apiKey,
        authentication=authentication,
        server_url=server_url,
        headers=headers,
        proxies=proxies,
    )
    return response.json() if json else response

@register_command(
    extending=("configurationadmin", "v1", "instance"),
    module=argus_cli_module
)
def delete_instance(
    id: int,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
) -> dict:
    """Delete configuration instance (INTERNAL)
    
    :param int id: ID of instance to delete
    :param json: return the response's body as a ``dict`` parsed from json. ``True`` by
      default. If set to false, the raw ``requests.Response`` object will be returned.
    :param verify: path to a certificate bundle or boolean indicating whether SSL
      verification should be performed.
    :param apiKey: Argus API key.
    :param authentication: authentication override
    :param server_url: API base URL override
    :param body: body of the request. other parameters will override keys defined in the body.
    :raises AuthenticationFailedException: on 401
    :raises AccessDeniedException: on 403
    :raises ObjectNotFoundException: on 404
    :raises ValidationErrorException: on 412
    :raises ArgusException: on other status codes
    
    :returns: dictionary translated from JSON
    """

    route = "/configurationadmin/v1/instance/{id}".format(id=id)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

    query_parameters = {}
    log.debug("DELETE %s (headers: %s, body: %s)" % (route, str(headers), str(body) or ""))

    response = session.delete(
        route,
        params=query_parameters or None,
        verify=verify,
        apiKey=apiKey,
        authentication=authentication,
        server_url=server_url,
        headers=headers,
        proxies=proxies,
    )
    return response.json() if json else response

@register_command(
    extending=("configurationadmin", "v1", "instance"),
    module=argus_cli_module
)
def disable_instance_monitoring(
    id: int,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
) -> dict:
    """Disable monitoring of configuration instance (INTERNAL)
    
    :param int id: ID of instance to disable monitoring on
    :param json: return the response's body as a ``dict`` parsed from json. ``True`` by
      default. If set to false, the raw ``requests.Response`` object will be returned.
    :param verify: path to a certificate bundle or boolean indicating whether SSL
      verification should be performed.
    :param apiKey: Argus API key.
    :param authentication: authentication override
    :param server_url: API base URL override
    :param body: body of the request. other parameters will override keys defined in the body.
    :raises AuthenticationFailedException: on 401
    :raises AccessDeniedException: on 403
    :raises ObjectNotFoundException: on 404
    :raises ValidationErrorException: on 412
    :raises ArgusException: on other status codes
    
    :returns: dictionary translated from JSON
    """

    route = "/configurationadmin/v1/instance/{id}/monitoring/disable".format(id=id)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

    query_parameters = {}
    log.debug("PUT %s (headers: %s, body: %s)" % (route, str(headers), str(body) or ""))

    response = session.put(
        route,
        params=query_parameters or None,
        data=body or None,
        verify=verify,
        apiKey=apiKey,
        authentication=authentication,
        server_url=server_url,
        headers=headers,
        proxies=proxies,
    )
    return response.json() if json else response

@register_command(
    extending=("configurationadmin", "v1", "instance"),
    module=argus_cli_module
)
def duplicate_instance(
    instanceID: int,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
) -> dict:
    """Duplicate a configuration instance (INTERNAL)
    
    :param int instanceID: ID of instance to duplicate
    :param json: return the response's body as a ``dict`` parsed from json. ``True`` by
      default. If set to false, the raw ``requests.Response`` object will be returned.
    :param verify: path to a certificate bundle or boolean indicating whether SSL
      verification should be performed.
    :param apiKey: Argus API key.
    :param authentication: authentication override
    :param server_url: API base URL override
    :param body: body of the request. other parameters will override keys defined in the body.
    :raises AuthenticationFailedException: on 401
    :raises AccessDeniedException: on 403
    :raises ObjectNotFoundException: on 404
    :raises ValidationErrorException: on 412
    :raises ArgusException: on other status codes
    
    :returns: dictionary translated from JSON
    """

    route = "/configurationadmin/v1/instance/{instanceID}/duplicate".format(instanceID=instanceID)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

    query_parameters = {}
    log.debug("POST %s (headers: %s, body: %s)" % (route, str(headers), str(body) or ""))

    response = session.post(
        route,
        params=query_parameters or None,
        data=body or None,
        verify=verify,
        apiKey=apiKey,
        authentication=authentication,
        server_url=server_url,
        headers=headers,
        proxies=proxies,
    )
    return response.json() if json else response

@register_command(
    extending=("configurationadmin", "v1", "instance"),
    module=argus_cli_module
)
def enable_instance_monitoring(
    id: int,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
) -> dict:
    """Enable monitoring of configuration instance (INTERNAL)
    
    :param int id: ID of instance to enable monitoring on
    :param json: return the response's body as a ``dict`` parsed from json. ``True`` by
      default. If set to false, the raw ``requests.Response`` object will be returned.
    :param verify: path to a certificate bundle or boolean indicating whether SSL
      verification should be performed.
    :param apiKey: Argus API key.
    :param authentication: authentication override
    :param server_url: API base URL override
    :param body: body of the request. other parameters will override keys defined in the body.
    :raises AuthenticationFailedException: on 401
    :raises AccessDeniedException: on 403
    :raises ObjectNotFoundException: on 404
    :raises ValidationErrorException: on 412
    :raises ArgusException: on other status codes
    
    :returns: dictionary translated from JSON
    """

    route = "/configurationadmin/v1/instance/{id}/monitoring/enable".format(id=id)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

    query_parameters = {}
    log.debug("PUT %s (headers: %s, body: %s)" % (route, str(headers), str(body) or ""))

    response = session.put(
        route,
        params=query_parameters or None,
        json=body,
        verify=verify,
        apiKey=apiKey,
        authentication=authentication,
        server_url=server_url,
        headers=headers,
        proxies=proxies,
    )
    return response.json() if json else response

@register_command(
    extending=("configurationadmin", "v1", "instance"),
    module=argus_cli_module
)
def instance_revisions(
    id: int,
    offset: int = None,
    limit: int = 25,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
) -> dict:
    """List configuration instance revisions (INTERNAL)
    
    :param int id: ID of instance to fetch revisions for
    :param int offset: Offset results
    :param int limit: Limit results
    :param json: return the response's body as a ``dict`` parsed from json. ``True`` by
      default. If set to false, the raw ``requests.Response`` object will be returned.
    :param verify: path to a certificate bundle or boolean indicating whether SSL
      verification should be performed.
    :param apiKey: Argus API key.
    :param authentication: authentication override
    :param server_url: API base URL override
    :param body: body of the request. other parameters will override keys defined in the body.
    :raises AuthenticationFailedException: on 401
    :raises AccessDeniedException: on 403
    :raises ObjectNotFoundException: on 404
    :raises ValidationErrorException: on 412
    :raises ArgusException: on other status codes
    
    :returns: dictionary translated from JSON
    """

    route = "/configurationadmin/v1/instance/{id}/revisions".format(limit=limit,
        id=id,
        offset=offset)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

    query_parameters = {}
    # Only send limit if the argument was provided, dont send null values
    if limit is not None:
        query_parameters.update({"limit": limit})
    
    # Only send offset if the argument was provided, dont send null values
    if offset is not None:
        query_parameters.update({"offset": offset})
    
    log.debug("GET %s (headers: %s, body: %s)" % (route, str(headers), str(body) or ""))

    response = session.get(
        route,
        params=query_parameters or None,
        verify=verify,
        apiKey=apiKey,
        authentication=authentication,
        server_url=server_url,
        headers=headers,
        proxies=proxies,
    )
    return response.json() if json else response

@register_command(
    extending=("configurationadmin", "v1", "instance"),
    module=argus_cli_module
)
def list_instances(
    offset: int = None,
    search: str = None,
    includeComments: bool = None,
    includeDeleted: bool = None,
    templateID: int = None,
    hostID: int = None,
    limit: int = 25,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
) -> dict:
    """List configuration instances (INTERNAL)
    
    :param int offset: Offset results
    :param str search: Limit results to instances matching this searchstring
    :param bool includeComments: Include comments in output
    :param bool includeDeleted: Include deleted instances
    :param list templateID: Limit results to instances with these templates
    :param list hostID: Limit results to instances on these hosts
    :param int limit: Limit results
    :param json: return the response's body as a ``dict`` parsed from json. ``True`` by
      default. If set to false, the raw ``requests.Response`` object will be returned.
    :param verify: path to a certificate bundle or boolean indicating whether SSL
      verification should be performed.
    :param apiKey: Argus API key.
    :param authentication: authentication override
    :param server_url: API base URL override
    :param body: body of the request. other parameters will override keys defined in the body.
    :raises AuthenticationFailedException: on 401
    :raises AccessDeniedException: on 403
    :raises ValidationErrorException: on 412
    :raises ArgusException: on other status codes
    
    :returns: dictionary translated from JSON
    """

    route = "/configurationadmin/v1/instance".format(limit=limit,
        offset=offset,
        search=search,
        includeComments=includeComments,
        includeDeleted=includeDeleted,
        templateID=templateID,
        hostID=hostID)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

    query_parameters = {}
    # Only send limit if the argument was provided, dont send null values
    if limit is not None:
        query_parameters.update({"limit": limit})
    
    # Only send offset if the argument was provided, dont send null values
    if offset is not None:
        query_parameters.update({"offset": offset})
    
    # Only send search if the argument was provided, dont send null values
    if search is not None:
        query_parameters.update({"search": search})
    
    # Only send includeComments if the argument was provided, dont send null values
    if includeComments is not None:
        query_parameters.update({"includeComments": includeComments})
    
    # Only send includeDeleted if the argument was provided, dont send null values
    if includeDeleted is not None:
        query_parameters.update({"includeDeleted": includeDeleted})
    
    # Only send templateID if the argument was provided, dont send null values
    if templateID is not None:
        query_parameters.update({"templateID": templateID})
    
    # Only send hostID if the argument was provided, dont send null values
    if hostID is not None:
        query_parameters.update({"hostID": hostID})
    
    log.debug("GET %s (headers: %s, body: %s)" % (route, str(headers), str(body) or ""))

    response = session.get(
        route,
        params=query_parameters or None,
        verify=verify,
        apiKey=apiKey,
        authentication=authentication,
        server_url=server_url,
        headers=headers,
        proxies=proxies,
    )
    return response.json() if json else response

@register_command(
    extending=("configurationadmin", "v1", "instance"),
    module=argus_cli_module
)
def schedule_instance_monitoring(
    id: int,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
) -> dict:
    """Schedule downtime for configuration instance (INTERNAL)
    
    :param int id: ID of instance to schedule downtime for
    :param json: return the response's body as a ``dict`` parsed from json. ``True`` by
      default. If set to false, the raw ``requests.Response`` object will be returned.
    :param verify: path to a certificate bundle or boolean indicating whether SSL
      verification should be performed.
    :param apiKey: Argus API key.
    :param authentication: authentication override
    :param server_url: API base URL override
    :param body: body of the request. other parameters will override keys defined in the body.
    :raises AuthenticationFailedException: on 401
    :raises AccessDeniedException: on 403
    :raises ObjectNotFoundException: on 404
    :raises ValidationErrorException: on 412
    :raises ArgusException: on other status codes
    
    :returns: dictionary translated from JSON
    """

    route = "/configurationadmin/v1/instance/{id}/monitoring/schedule".format(id=id)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

    query_parameters = {}
    log.debug("PUT %s (headers: %s, body: %s)" % (route, str(headers), str(body) or ""))

    response = session.put(
        route,
        params=query_parameters or None,
        data=body or None,
        verify=verify,
        apiKey=apiKey,
        authentication=authentication,
        server_url=server_url,
        headers=headers,
        proxies=proxies,
    )
    return response.json() if json else response

@register_command(
    extending=("configurationadmin", "v1", "instance"),
    module=argus_cli_module
)
def search_instances(
    instanceID: int = None,
    templateID: int = None,
    hostID: int = None,
    limit: int = None,
    offset: int = None,
    includeDeleted: bool = None,
    includeFlags: int = None,
    excludeFlags: int = None,
    subCriteria: dict = None,
    exclude: bool = None,
    required: bool = None,
    template: str = None,
    instance: int = None,
    host: str = None,
    parentID: int = None,
    codeProfile: str = None,
    keywords: str = None,
    masterID: int = None,
    codeProfileOverride: bool = None,
    inDowntime: bool = None,
    sortBy: str = None,
    includeComments: bool = None,
    includeProperties: bool = True,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
) -> dict:
    """Search configuration instances (INTERNAL)
    
    :param list instanceID: 
    :param list templateID: 
    :param list hostID: 
    :param int limit: Max number of results.
    :param int offset: Skip the first \(offset\) objects. By default\, return result from first object.
    :param bool includeDeleted: Set to true to include deleted objects. By default\, exclude deleted objects.
    :param int includeFlags: Only include objects which have includeFlags set.
    :param int excludeFlags: Exclude objects which have excludeFlags set.
    :param list subCriteria: Set additional criterias which are applied using a logical OR.
    :param bool exclude: Only relevant for subcriteria. If set to true\, objects matching this subcriteria object will be excluded.
    :param bool required: Only relevant for subcriteria. If set to true\, objects matching this subcriteria are required \(AND\-ed together with parent criteria\).
    :param list template: If set\, filter instances by template ID or shortname.
    :param list instance: If set\, filter instances by ID.
    :param list host: If set\, filter instances by host ID or hostname.
    :param list parentID: If set\, filter instances by parent instance ID.
    :param list codeProfile: If set\, filter instances by active code profile.
    :param list keywords: If set\, filter instances matching these keywords.
    :param int masterID: If set\, only include instance revisions of given master. If not set\, revisions are excluded.
    :param bool codeProfileOverride: If true\, only return instances with overridden code profile. If false\, exclude. If not set\, do not filter.
    :param bool inDowntime: If true\, only return instances which are in scheduled downtime\, or whose host is in downtime. If false\, exclude. If not set\, do not filter.
    :param list sortBy: List of properties to sort by \(prefix with \"\-\" to sort descending\).
    :param bool includeComments: If true\, include comments in output. \(default false\)
    :param bool includeProperties: If true\, include properties in output. \(default true\)
    :param json: return the response's body as a ``dict`` parsed from json. ``True`` by
      default. If set to false, the raw ``requests.Response`` object will be returned.
    :param verify: path to a certificate bundle or boolean indicating whether SSL
      verification should be performed.
    :param apiKey: Argus API key.
    :param authentication: authentication override
    :param server_url: API base URL override
    :param body: body of the request. other parameters will override keys defined in the body.
    :raises AuthenticationFailedException: on 401
    :raises AccessDeniedException: on 403
    :raises ValidationErrorException: on 412
    :raises ArgusException: on other status codes
    
    :returns: dictionary translated from JSON
    """

    route = "/configurationadmin/v1/instance/search".format()

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}
    # Only send instanceID if the argument was provided, dont send null values
    if instanceID is not None:
        body.update({"instanceID": instanceID})
    # Only send templateID if the argument was provided, dont send null values
    if templateID is not None:
        body.update({"templateID": templateID})
    # Only send hostID if the argument was provided, dont send null values
    if hostID is not None:
        body.update({"hostID": hostID})
    # Only send limit if the argument was provided, dont send null values
    if limit is not None:
        body.update({"limit": limit})
    # Only send offset if the argument was provided, dont send null values
    if offset is not None:
        body.update({"offset": offset})
    # Only send includeDeleted if the argument was provided, dont send null values
    if includeDeleted is not None:
        body.update({"includeDeleted": includeDeleted})
    # Only send includeFlags if the argument was provided, dont send null values
    if includeFlags is not None:
        body.update({"includeFlags": includeFlags})
    # Only send excludeFlags if the argument was provided, dont send null values
    if excludeFlags is not None:
        body.update({"excludeFlags": excludeFlags})
    # Only send subCriteria if the argument was provided, dont send null values
    if subCriteria is not None:
        body.update({"subCriteria": subCriteria})
    # Only send exclude if the argument was provided, dont send null values
    if exclude is not None:
        body.update({"exclude": exclude})
    # Only send required if the argument was provided, dont send null values
    if required is not None:
        body.update({"required": required})
    # Only send includeComments if the argument was provided, dont send null values
    if includeComments is not None:
        body.update({"includeComments": includeComments})
    # Only send includeProperties if the argument was provided, dont send null values
    if includeProperties is not None:
        body.update({"includeProperties": includeProperties})
    # Only send template if the argument was provided, dont send null values
    if template is not None:
        body.update({"template": template})
    # Only send instance if the argument was provided, dont send null values
    if instance is not None:
        body.update({"instance": instance})
    # Only send host if the argument was provided, dont send null values
    if host is not None:
        body.update({"host": host})
    # Only send parentID if the argument was provided, dont send null values
    if parentID is not None:
        body.update({"parentID": parentID})
    # Only send codeProfile if the argument was provided, dont send null values
    if codeProfile is not None:
        body.update({"codeProfile": codeProfile})
    # Only send keywords if the argument was provided, dont send null values
    if keywords is not None:
        body.update({"keywords": keywords})
    # Only send masterID if the argument was provided, dont send null values
    if masterID is not None:
        body.update({"masterID": masterID})
    # Only send codeProfileOverride if the argument was provided, dont send null values
    if codeProfileOverride is not None:
        body.update({"codeProfileOverride": codeProfileOverride})
    # Only send inDowntime if the argument was provided, dont send null values
    if inDowntime is not None:
        body.update({"inDowntime": inDowntime})
    # Only send sortBy if the argument was provided, dont send null values
    if sortBy is not None:
        body.update({"sortBy": sortBy})

    query_parameters = {}
    log.debug("POST %s (headers: %s, body: %s)" % (route, str(headers), str(body) or ""))

    response = session.post(
        route,
        params=query_parameters or None,
        json=body,
        verify=verify,
        apiKey=apiKey,
        authentication=authentication,
        server_url=server_url,
        headers=headers,
        proxies=proxies,
    )
    return response.json() if json else response

@register_command(
    extending=("configurationadmin", "v1", "instance"),
    module=argus_cli_module
)
def update_instance(
    id: int,
    configurationID: int = None,
    hostID: int = None,
    parentID: int = None,
    information: str = None,
    properties: dict = None,
    identifiers: dict = None,
    codeProfile: str = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
) -> dict:
    """Update configuration instance (INTERNAL)
    
    :param int id: ID of instance to update
    :param int configurationID: 
    :param int hostID: If set\, assign instance to given configuration host.
    :param int parentID: If set\, set parent instance for this instance \(on same configuration host\).
    :param str information: If set\, change information field for instance. \=\> \[\\s\\w\\\{\\\}\\\$\\\-\\\(\\\)\\.\\\[\\\]\"\\\'\_\/\\\\\,\\\*\\\+\\\#\:\@\!\?\;\=\]\*
    :param dict properties: If set\, set these properties for instance. Property with null value will delete existing property.
    :param dict identifiers: If set\, set these identifiers for instance. Identifier with null value will delete existing identifier.
    :param str codeProfile: Name of code profile to use. If null\, do not change. If blank\, reset to template profile. \=\> \[a\-zA\-Z0\-9\_\\\-\\.\]\*
    :param json: return the response's body as a ``dict`` parsed from json. ``True`` by
      default. If set to false, the raw ``requests.Response`` object will be returned.
    :param verify: path to a certificate bundle or boolean indicating whether SSL
      verification should be performed.
    :param apiKey: Argus API key.
    :param authentication: authentication override
    :param server_url: API base URL override
    :param body: body of the request. other parameters will override keys defined in the body.
    :raises AuthenticationFailedException: on 401
    :raises AccessDeniedException: on 403
    :raises ObjectNotFoundException: on 404
    :raises ValidationErrorException: on 412
    :raises ArgusException: on other status codes
    
    :returns: dictionary translated from JSON
    """

    route = "/configurationadmin/v1/instance/{id}".format(id=id)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}
    # Only send id if the argument was provided, dont send null values
    if id is not None:
        body.update({"id": id})
    # Only send configurationID if the argument was provided, dont send null values
    if configurationID is not None:
        body.update({"configurationID": configurationID})
    # Only send hostID if the argument was provided, dont send null values
    if hostID is not None:
        body.update({"hostID": hostID})
    # Only send parentID if the argument was provided, dont send null values
    if parentID is not None:
        body.update({"parentID": parentID})
    # Only send information if the argument was provided, dont send null values
    if information is not None:
        body.update({"information": information})
    # Only send properties if the argument was provided, dont send null values
    if properties is not None:
        body.update({"properties": properties})
    # Only send identifiers if the argument was provided, dont send null values
    if identifiers is not None:
        body.update({"identifiers": identifiers})
    # Only send codeProfile if the argument was provided, dont send null values
    if codeProfile is not None:
        body.update({"codeProfile": codeProfile})

    query_parameters = {}
    log.debug("PUT %s (headers: %s, body: %s)" % (route, str(headers), str(body) or ""))

    response = session.put(
        route,
        params=query_parameters or None,
        json=body,
        verify=verify,
        apiKey=apiKey,
        authentication=authentication,
        server_url=server_url,
        headers=headers,
        proxies=proxies,
    )
    return response.json() if json else response

@register_command(
    extending=("configurationadmin", "v1", "instance"),
    module=argus_cli_module
)
def view_instance(
    id: int,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
) -> dict:
    """Fetch configuration instance (INTERNAL)
    
    :param int id: ID of instance to fetch
    :param json: return the response's body as a ``dict`` parsed from json. ``True`` by
      default. If set to false, the raw ``requests.Response`` object will be returned.
    :param verify: path to a certificate bundle or boolean indicating whether SSL
      verification should be performed.
    :param apiKey: Argus API key.
    :param authentication: authentication override
    :param server_url: API base URL override
    :param body: body of the request. other parameters will override keys defined in the body.
    :raises AuthenticationFailedException: on 401
    :raises AccessDeniedException: on 403
    :raises ObjectNotFoundException: on 404
    :raises ValidationErrorException: on 412
    :raises ArgusException: on other status codes
    
    :returns: dictionary translated from JSON
    """

    route = "/configurationadmin/v1/instance/{id}".format(id=id)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

    query_parameters = {}
    log.debug("GET %s (headers: %s, body: %s)" % (route, str(headers), str(body) or ""))

    response = session.get(
        route,
        params=query_parameters or None,
        verify=verify,
        apiKey=apiKey,
        authentication=authentication,
        server_url=server_url,
        headers=headers,
        proxies=proxies,
    )
    return response.json() if json else response

#: **DEPRECATED** : ``add_comment_1`` is an alias for ``add_instance_comment``. Exists
#: only for backward compatibility - **do not use** - use ``add_instance_comment`` instead.
add_comment_1 = register_command(
    extending=("configurationadmin", "v1", "instance"),
    module=argus_cli_module,
    alias="add_comment_1"
)(deprecated_alias("add_comment_1")(add_instance_comment))
#: **DEPRECATED** : ``create_3`` is an alias for ``create_instance``. Exists
#: only for backward compatibility - **do not use** - use ``create_instance`` instead.
create_3 = register_command(
    extending=("configurationadmin", "v1", "instance"),
    module=argus_cli_module,
    alias="create_3"
)(deprecated_alias("create_3")(create_instance))
#: **DEPRECATED** : ``delete_2`` is an alias for ``delete_instance``. Exists
#: only for backward compatibility - **do not use** - use ``delete_instance`` instead.
delete_2 = register_command(
    extending=("configurationadmin", "v1", "instance"),
    module=argus_cli_module,
    alias="delete_2"
)(deprecated_alias("delete_2")(delete_instance))
#: **DEPRECATED** : ``disable_monitoring_1`` is an alias for ``disable_instance_monitoring``. Exists
#: only for backward compatibility - **do not use** - use ``disable_instance_monitoring`` instead.
disable_monitoring_1 = register_command(
    extending=("configurationadmin", "v1", "instance"),
    module=argus_cli_module,
    alias="disable_monitoring_1"
)(deprecated_alias("disable_monitoring_1")(disable_instance_monitoring))
#: **DEPRECATED** : ``enable_monitoring_1`` is an alias for ``enable_instance_monitoring``. Exists
#: only for backward compatibility - **do not use** - use ``enable_instance_monitoring`` instead.
enable_monitoring_1 = register_command(
    extending=("configurationadmin", "v1", "instance"),
    module=argus_cli_module,
    alias="enable_monitoring_1"
)(deprecated_alias("enable_monitoring_1")(enable_instance_monitoring))
#: **DEPRECATED** : ``revisions`` is an alias for ``instance_revisions``. Exists
#: only for backward compatibility - **do not use** - use ``instance_revisions`` instead.
revisions = register_command(
    extending=("configurationadmin", "v1", "instance"),
    module=argus_cli_module,
    alias="revisions"
)(deprecated_alias("revisions")(instance_revisions))
#: **DEPRECATED** : ``list_3`` is an alias for ``list_instances``. Exists
#: only for backward compatibility - **do not use** - use ``list_instances`` instead.
list_3 = register_command(
    extending=("configurationadmin", "v1", "instance"),
    module=argus_cli_module,
    alias="list_3"
)(deprecated_alias("list_3")(list_instances))
#: **DEPRECATED** : ``schedule_monitoring_1`` is an alias for ``schedule_instance_monitoring``. Exists
#: only for backward compatibility - **do not use** - use ``schedule_instance_monitoring`` instead.
schedule_monitoring_1 = register_command(
    extending=("configurationadmin", "v1", "instance"),
    module=argus_cli_module,
    alias="schedule_monitoring_1"
)(deprecated_alias("schedule_monitoring_1")(schedule_instance_monitoring))
#: **DEPRECATED** : ``search_3`` is an alias for ``search_instances``. Exists
#: only for backward compatibility - **do not use** - use ``search_instances`` instead.
search_3 = register_command(
    extending=("configurationadmin", "v1", "instance"),
    module=argus_cli_module,
    alias="search_3"
)(deprecated_alias("search_3")(search_instances))
#: **DEPRECATED** : ``update_2`` is an alias for ``update_instance``. Exists
#: only for backward compatibility - **do not use** - use ``update_instance`` instead.
update_2 = register_command(
    extending=("configurationadmin", "v1", "instance"),
    module=argus_cli_module,
    alias="update_2"
)(deprecated_alias("update_2")(update_instance))
#: **DEPRECATED** : ``update_2`` is an alias for ``update_instance``. Exists
#: only for backward compatibility - **do not use** - use ``update_instance`` instead.
update_2 = register_command(
    extending=("configurationadmin", "v1", "instance"),
    module=argus_cli_module,
    alias="update_2"
)(deprecated_alias("update_2")(update_instance))
#: **DEPRECATED** : ``view_1`` is an alias for ``view_instance``. Exists
#: only for backward compatibility - **do not use** - use ``view_instance`` instead.
view_1 = register_command(
    extending=("configurationadmin", "v1", "instance"),
    module=argus_cli_module,
    alias="view_1"
)(deprecated_alias("view_1")(view_instance))
#: **DEPRECATED** : ``duplicate_host_1`` is an alias for ``duplicate_instance``. Exists
#: only for backward compatibility - **do not use** - use ``duplicate_instance`` instead.
duplicate_host_1 = register_command(
    extending=("configurationadmin", "v1", "instance"),
    module=argus_cli_module,
    alias="duplicate_host_1"
)(deprecated_alias("duplicate_host_1")(duplicate_instance))