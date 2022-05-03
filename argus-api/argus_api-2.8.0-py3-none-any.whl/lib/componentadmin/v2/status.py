"""Autogenerated API"""
from argus_api import session
from argus_api.utils import deprecated_alias


def get_component_status(
    componentID: str,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
) -> dict:
    """Fetch status for specified component (INTERNAL)
    
    :param str componentID: Component ID
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

    route = "/componentadmin/v2/status/component/{componentID}".format(componentID=componentID)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

    query_parameters = {}

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


def get_host_instances(
    host: str,
    limit: int = 25,
    offset: int = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
) -> dict:
    """Request status for all instances on specified host (INTERNAL)
    
    :param str host: ID or name of host to request instance status for
    :param int limit: Maximum number of results\, or 0 for unlimited. Default is 25.
    :param int offset: Skip this number of results.
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

    route = "/componentadmin/v2/status/host/{host}/instances".format(limit=limit,
        host=host,
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


def get_host_status(
    host: str,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
) -> dict:
    """Request status for specific host (INTERNAL)
    
    :param str host: ID or name of host to request status for
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

    route = "/componentadmin/v2/status/host/{host}".format(host=host)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

    query_parameters = {}

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


def get_instance_status(
    instanceID: int,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
) -> dict:
    """Request status for specific instance (INTERNAL)
    
    :param int instanceID: ID of instance to request status for
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

    route = "/componentadmin/v2/status/instance/{instanceID}".format(instanceID=instanceID)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

    query_parameters = {}

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


def get_status_overview(
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
) -> dict:
    """Request status overview (INTERNAL)
    
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

    route = "/componentadmin/v2/status".format()

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

    query_parameters = {}

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


def list_component_status(
    componentType: str = None,
    limit: int = 25,
    offset: int = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
) -> dict:
    """List component status (INTERNAL)
    
    :param str componentType: Component type
    :param int limit: Maximum number of results\, or 0 for unlimited. Default is 25.
    :param int offset: Skip this number of results.
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

    route = "/componentadmin/v2/status/component".format(limit=limit,
        componentType=componentType,
        offset=offset)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

    query_parameters = {}
    # Only send limit if the argument was provided, dont send null values
    if limit is not None:
        query_parameters.update({"limit": limit})
    
    # Only send componentType if the argument was provided, dont send null values
    if componentType is not None:
        query_parameters.update({"componentType": componentType})
    
    # Only send offset if the argument was provided, dont send null values
    if offset is not None:
        query_parameters.update({"offset": offset})
    

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


def list_host_status(
    instanceState: str = None,
    hostState: str = None,
    sortBy: str = None,
    limit: int = 25,
    offset: int = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
) -> dict:
    """Simple host status search (INTERNAL)
    
    :param list instanceState: Filter result by instance state
    :param list hostState: Filter result by host state
    :param list sortBy: Specify sort ordering. Default is sort by name ascending.
    :param int limit: Maximum number of results\, or 0 for unlimited. Default is 25.
    :param int offset: Skip this number of results.
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

    route = "/componentadmin/v2/status/host".format(limit=limit,
        instanceState=instanceState,
        hostState=hostState,
        offset=offset,
        sortBy=sortBy)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

    query_parameters = {}
    # Only send limit if the argument was provided, dont send null values
    if limit is not None:
        query_parameters.update({"limit": limit})
    
    # Only send instanceState if the argument was provided, dont send null values
    if instanceState is not None:
        query_parameters.update({"instanceState": instanceState})
    
    # Only send hostState if the argument was provided, dont send null values
    if hostState is not None:
        query_parameters.update({"hostState": hostState})
    
    # Only send offset if the argument was provided, dont send null values
    if offset is not None:
        query_parameters.update({"offset": offset})
    
    # Only send sortBy if the argument was provided, dont send null values
    if sortBy is not None:
        query_parameters.update({"sortBy": sortBy})
    

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


def list_instance_status(
    instanceState: str = None,
    limit: int = 25,
    offset: int = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
) -> dict:
    """Simple instance status search (INTERNAL)
    
    :param list instanceState: Filter result by instance state
    :param int limit: Maximum number of results\, or 0 for unlimited. Default is 25.
    :param int offset: Skip this number of results.
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

    route = "/componentadmin/v2/status/instance".format(limit=limit,
        instanceState=instanceState,
        offset=offset)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

    query_parameters = {}
    # Only send limit if the argument was provided, dont send null values
    if limit is not None:
        query_parameters.update({"limit": limit})
    
    # Only send instanceState if the argument was provided, dont send null values
    if instanceState is not None:
        query_parameters.update({"instanceState": instanceState})
    
    # Only send offset if the argument was provided, dont send null values
    if offset is not None:
        query_parameters.update({"offset": offset})
    

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


def search_component_status(
    componentType: str = None,
    componentIdentifiers: dict = None,
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
    """Advanced component status search (INTERNAL)
    
    :param str componentType: Type of components to invoke
    :param dict componentIdentifiers: Identifiers of components to invoke
    :param int offset: Set this value to skip the first \(offset\) objects. By default\, return result from first object.
    :param int limit: Set this value to set max number of results. By default\, result set size is 25. \(default 25\)
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

    route = "/componentadmin/v2/status/component/search".format()

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}
    # Only send componentType if the argument was provided, dont send null values
    if componentType is not None:
        body.update({"componentType": componentType})
    # Only send componentIdentifiers if the argument was provided, dont send null values
    if componentIdentifiers is not None:
        body.update({"componentIdentifiers": componentIdentifiers})
    # Only send limit if the argument was provided, dont send null values
    if limit is not None:
        body.update({"limit": limit})
    # Only send offset if the argument was provided, dont send null values
    if offset is not None:
        body.update({"offset": offset})

    query_parameters = {}

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


def search_host_status(
    keywords: str = None,
    state: str = None,
    includeFlags: str = None,
    excludeFlags: str = None,
    subCriteria: dict = None,
    instanceCriteria: dict = None,
    offset: int = None,
    sortBy: str = None,
    limit: int = 25,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
) -> dict:
    """Advanced host status search (INTERNAL)
    
    :param list keywords: A set of keywords matched against hosts.
    :param list state: If set\, limit result to hosts in one of these states.
    :param list includeFlags: If set\, include only results where all these flags are set.
    :param list excludeFlags: If set\, exclude all results where all these flags are set.
    :param list subCriteria: Set additional criterias \(by default applied using a logical OR\, unless required\/excluded is set\).
    :param list instanceCriteria: Filter hosts by instance status search criteria. Will filter hosts which contain the matching instances
    :param int offset: Set this value to skip the first \(offset\) objects. By default\, return result from first object.
    :param list sortBy: Specify sort ordering for returned host status. Default is sort by host name. \(default \[name\]\)
    :param int limit: Set this value to set max number of results. By default\, result set size is 25. \(default 25\)
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

    route = "/componentadmin/v2/status/host/search".format()

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}
    # Only send keywords if the argument was provided, dont send null values
    if keywords is not None:
        body.update({"keywords": keywords})
    # Only send state if the argument was provided, dont send null values
    if state is not None:
        body.update({"state": state})
    # Only send includeFlags if the argument was provided, dont send null values
    if includeFlags is not None:
        body.update({"includeFlags": includeFlags})
    # Only send excludeFlags if the argument was provided, dont send null values
    if excludeFlags is not None:
        body.update({"excludeFlags": excludeFlags})
    # Only send subCriteria if the argument was provided, dont send null values
    if subCriteria is not None:
        body.update({"subCriteria": subCriteria})
    # Only send instanceCriteria if the argument was provided, dont send null values
    if instanceCriteria is not None:
        body.update({"instanceCriteria": instanceCriteria})
    # Only send limit if the argument was provided, dont send null values
    if limit is not None:
        body.update({"limit": limit})
    # Only send offset if the argument was provided, dont send null values
    if offset is not None:
        body.update({"offset": offset})
    # Only send sortBy if the argument was provided, dont send null values
    if sortBy is not None:
        body.update({"sortBy": sortBy})

    query_parameters = {}

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


def search_instance_status(
    keywords: str = None,
    host: str = None,
    template: str = None,
    state: str = None,
    includeFlags: str = None,
    excludeFlags: str = None,
    subCriteria: dict = None,
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
    """Advanced instance status search (INTERNAL)
    
    :param list keywords: A set of keywords matched against instances\, or their template or host.
    :param list host: If set\, limit result to instances for any of these hosts \(by id or hostname\).
    :param list template: If set\, limit result to instances of any of these templates \(by id or shortname\)
    :param list state: If set\, limit result to instances in one of these states.
    :param list includeFlags: If set\, include only results where all these flags are set.
    :param list excludeFlags: If set\, exclude all results where all these flags are set.
    :param list subCriteria: Set additional criterias \(by default applied using a logical OR\, unless required\/excluded is set\).
    :param int offset: Set this value to skip the first \(offset\) objects. By default\, return result from first object.
    :param int limit: Set this value to set max number of results. By default\, result set size is 25. \(default 25\)
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

    route = "/componentadmin/v2/status/instance/search".format()

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}
    # Only send keywords if the argument was provided, dont send null values
    if keywords is not None:
        body.update({"keywords": keywords})
    # Only send host if the argument was provided, dont send null values
    if host is not None:
        body.update({"host": host})
    # Only send template if the argument was provided, dont send null values
    if template is not None:
        body.update({"template": template})
    # Only send state if the argument was provided, dont send null values
    if state is not None:
        body.update({"state": state})
    # Only send includeFlags if the argument was provided, dont send null values
    if includeFlags is not None:
        body.update({"includeFlags": includeFlags})
    # Only send excludeFlags if the argument was provided, dont send null values
    if excludeFlags is not None:
        body.update({"excludeFlags": excludeFlags})
    # Only send subCriteria if the argument was provided, dont send null values
    if subCriteria is not None:
        body.update({"subCriteria": subCriteria})
    # Only send limit if the argument was provided, dont send null values
    if limit is not None:
        body.update({"limit": limit})
    # Only send offset if the argument was provided, dont send null values
    if offset is not None:
        body.update({"offset": offset})

    query_parameters = {}

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


def update_host_status(
    containerID: str = None,
    identifiers: dict = None,
    state: str = None,
    components: dict = None,
    containers: dict = None,
    installedContainers: dict = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
) -> dict:
    """Submit status update for a host which may also have running containers. The host will be resolved by agent using the current user. (INTERNAL)
    
    :param str containerID: ID of the currently running container
    :param dict identifiers: Any identifiers for this instance container
    :param str state: The state of this instance container
    :param list components: An optional list of component updates for the root container
    :param list containers: A set of instance container status records
    :param list installedContainers: A set of installed instance descriptors
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
    :raises ArgusException: on other status codes
    
    :returns: dictionary translated from JSON
    """

    route = "/componentadmin/v2/status".format()

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}
    # Only send containerID if the argument was provided, dont send null values
    if containerID is not None:
        body.update({"containerID": containerID})
    # Only send identifiers if the argument was provided, dont send null values
    if identifiers is not None:
        body.update({"identifiers": identifiers})
    # Only send state if the argument was provided, dont send null values
    if state is not None:
        body.update({"state": state})
    # Only send components if the argument was provided, dont send null values
    if components is not None:
        body.update({"components": components})
    # Only send containers if the argument was provided, dont send null values
    if containers is not None:
        body.update({"containers": containers})
    # Only send installedContainers if the argument was provided, dont send null values
    if installedContainers is not None:
        body.update({"installedContainers": installedContainers})

    query_parameters = {}

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


def update_instance_status(
    instanceID: int,
    containerID: str = None,
    identifiers: dict = None,
    state: str = None,
    components: dict = None,
    runningInstanceRevision: int = None,
    runningTemplateRevision: int = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
) -> dict:
    """Submit status update for a specific component. The host will be resolved by agent using the current user.The instanceID must be a valid instance for the current users host. (INTERNAL)
    
    :param int instanceID: ID of instance
    :param str containerID: ID of the currently running container
    :param dict identifiers: Any identifiers for this instance container
    :param str state: The state of this instance container
    :param list components: An optional list of component updates for the root container
    :param int runningInstanceRevision: The instance revision of the running container
    :param int runningTemplateRevision: The template revision of the running container
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
    :raises ArgusException: on other status codes
    
    :returns: dictionary translated from JSON
    """

    route = "/componentadmin/v2/status/instance/{instanceID}".format(instanceID=instanceID)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}
    # Only send containerID if the argument was provided, dont send null values
    if containerID is not None:
        body.update({"containerID": containerID})
    # Only send identifiers if the argument was provided, dont send null values
    if identifiers is not None:
        body.update({"identifiers": identifiers})
    # Only send state if the argument was provided, dont send null values
    if state is not None:
        body.update({"state": state})
    # Only send components if the argument was provided, dont send null values
    if components is not None:
        body.update({"components": components})
    # Only send instanceID if the argument was provided, dont send null values
    if instanceID is not None:
        body.update({"instanceID": instanceID})
    # Only send runningInstanceRevision if the argument was provided, dont send null values
    if runningInstanceRevision is not None:
        body.update({"runningInstanceRevision": runningInstanceRevision})
    # Only send runningTemplateRevision if the argument was provided, dont send null values
    if runningTemplateRevision is not None:
        body.update({"runningTemplateRevision": runningTemplateRevision})

    query_parameters = {}

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

#: **DEPRECATED** : ``get_instance_status_1`` is an alias for ``get_instance_status``. Exists
#: only for backward compatibility - **do not use** - use ``get_instance_status`` instead.
get_instance_status_1 = deprecated_alias("get_instance_status_1")(get_instance_status)