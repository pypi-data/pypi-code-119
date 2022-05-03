"""Autogenerated API"""
from argus_api import session


def add_new_source(
    private: bool = None,
    alias: str = None,
    name: str = None,
    useForReputationCalc: bool = None,
    enableSync: bool = None,
    monitored: bool = None,
    confidence: float = None,
    activePeriod: int = None,
    fudgePeriod: int = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
) -> dict:
    """Add reputation source (INTERNAL)
    
    :param bool private: 
    :param str alias: Source alias \=\> \[a\-zA\-Z0\-9\_\\\-\\.\]\*
    :param str name: Source name \=\> \[a\-zA\-Z0\-9\_\\\-\\.\]\*
    :param bool useForReputationCalc: If true\, enable reputation calculation using this source
    :param bool enableSync: If true\, enable remote sync of this source \(even if reputation calc is not enabled\)
    :param bool monitored: If true\, mark this source as monitored
    :param float confidence: Source confidence \(default 0.0\)
    :param int activePeriod: Source active period \(default 0\)
    :param int fudgePeriod: Source fudge period \(default 0\)
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

    route = "/reputation/v1/source".format()

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}
    # Only send private if the argument was provided, dont send null values
    if private is not None:
        body.update({"private": private})
    # Only send alias if the argument was provided, dont send null values
    if alias is not None:
        body.update({"alias": alias})
    # Only send name if the argument was provided, dont send null values
    if name is not None:
        body.update({"name": name})
    # Only send confidence if the argument was provided, dont send null values
    if confidence is not None:
        body.update({"confidence": confidence})
    # Only send activePeriod if the argument was provided, dont send null values
    if activePeriod is not None:
        body.update({"activePeriod": activePeriod})
    # Only send fudgePeriod if the argument was provided, dont send null values
    if fudgePeriod is not None:
        body.update({"fudgePeriod": fudgePeriod})
    # Only send useForReputationCalc if the argument was provided, dont send null values
    if useForReputationCalc is not None:
        body.update({"useForReputationCalc": useForReputationCalc})
    # Only send enableSync if the argument was provided, dont send null values
    if enableSync is not None:
        body.update({"enableSync": enableSync})
    # Only send monitored if the argument was provided, dont send null values
    if monitored is not None:
        body.update({"monitored": monitored})

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


def delete_source(
    id: int,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
) -> dict:
    """Delete reputation source (INTERNAL)
    
    :param int id: ID of source to delete
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

    route = "/reputation/v1/source/{id}".format(id=id)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

    query_parameters = {}

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


def find_sources(
    id: int = None,
    searchString: str = None,
    limit: int = None,
    offset: int = None,
    includeDeleted: bool = None,
    includeFlags: int = None,
    excludeFlags: int = None,
    subCriteria: dict = None,
    exclude: bool = None,
    required: bool = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
) -> dict:
    """Search reputation sources (INTERNAL)
    
    :param list id: 
    :param str searchString: 
    :param int limit: Max number of results.
    :param int offset: Skip the first \(offset\) objects. By default\, return result from first object.
    :param bool includeDeleted: Set to true to include deleted objects. By default\, exclude deleted objects.
    :param int includeFlags: Only include objects which have includeFlags set.
    :param int excludeFlags: Exclude objects which have excludeFlags set.
    :param list subCriteria: Set additional criterias which are applied using a logical OR.
    :param bool exclude: Only relevant for subcriteria. If set to true\, objects matching this subcriteria object will be excluded.
    :param bool required: Only relevant for subcriteria. If set to true\, objects matching this subcriteria are required \(AND\-ed together with parent criteria\).
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

    route = "/reputation/v1/source/search".format()

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}
    # Only send id if the argument was provided, dont send null values
    if id is not None:
        body.update({"id": id})
    # Only send searchString if the argument was provided, dont send null values
    if searchString is not None:
        body.update({"searchString": searchString})
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


def get_source_by_alias(
    alias: str,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
) -> dict:
    """Fetch reputation source by alias (INTERNAL)
    
    :param str alias: Alias of source to fetch
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

    route = "/reputation/v1/source/{alias}".format(alias=alias)

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


def get_source_by_id(
    id: int,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
) -> dict:
    """Fetch reputation source by ID (INTERNAL)
    
    :param int id: ID of source to fetch
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

    route = "/reputation/v1/source/{id}".format(id=id)

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


def list_sources(
    search: str = None,
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
    """List reputation sources (INTERNAL)
    
    :param str search: Limit result to sources matching this search string
    :param int offset: Offset result
    :param int limit: Limit result
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

    route = "/reputation/v1/source".format(limit=limit,
        search=search,
        offset=offset)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

    query_parameters = {}
    # Only send limit if the argument was provided, dont send null values
    if limit is not None:
        query_parameters.update({"limit": limit})
    
    # Only send search if the argument was provided, dont send null values
    if search is not None:
        query_parameters.update({"search": search})
    
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


def transition_source(
    source: str,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
) -> dict:
    """Transition reputation source. This recalculates active and expired records according to the sources configured timing.Source Transition is automatically run after completing an import. (INTERNAL)
    
    :param str source: ID or alias of source to transition
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

    route = "/reputation/v1/source/{source}/transition".format(source=source)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

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


def update_source(
    id: int,
    alias: str = None,
    name: str = None,
    confidence: float = None,
    activePeriod: int = None,
    fudgePeriod: int = None,
    private: bool = None,
    useForReputationCalc: bool = None,
    enableSync: bool = None,
    monitored: bool = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
) -> dict:
    """Update reputation source (INTERNAL)
    
    :param int id: ID of source to update
    :param str alias: \[a\-zA\-Z0\-9\_\\\-\\.\]\*
    :param str name: \[a\-zA\-Z0\-9\_\\\-\\.\]\*
    :param float confidence: 
    :param int activePeriod: 
    :param int fudgePeriod: 
    :param bool private: 
    :param bool useForReputationCalc: If set\, change the setting for reputation calculation using this source
    :param bool enableSync: If set\, change the remote sync setting for this source
    :param bool monitored: If set\, change the monitored setting for this source
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

    route = "/reputation/v1/source/{id}".format(id=id)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}
    # Only send id if the argument was provided, dont send null values
    if id is not None:
        body.update({"id": id})
    # Only send alias if the argument was provided, dont send null values
    if alias is not None:
        body.update({"alias": alias})
    # Only send name if the argument was provided, dont send null values
    if name is not None:
        body.update({"name": name})
    # Only send confidence if the argument was provided, dont send null values
    if confidence is not None:
        body.update({"confidence": confidence})
    # Only send activePeriod if the argument was provided, dont send null values
    if activePeriod is not None:
        body.update({"activePeriod": activePeriod})
    # Only send fudgePeriod if the argument was provided, dont send null values
    if fudgePeriod is not None:
        body.update({"fudgePeriod": fudgePeriod})
    # Only send private if the argument was provided, dont send null values
    if private is not None:
        body.update({"private": private})
    # Only send useForReputationCalc if the argument was provided, dont send null values
    if useForReputationCalc is not None:
        body.update({"useForReputationCalc": useForReputationCalc})
    # Only send enableSync if the argument was provided, dont send null values
    if enableSync is not None:
        body.update({"enableSync": enableSync})
    # Only send monitored if the argument was provided, dont send null values
    if monitored is not None:
        body.update({"monitored": monitored})

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
