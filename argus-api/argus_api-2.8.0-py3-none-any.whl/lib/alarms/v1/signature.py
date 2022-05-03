"""Autogenerated API"""
from argus_api import session


def delete_signatures(
    signature: str,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
) -> dict:
    """Delete signatures. They must not be mapped to an alarm. (INTERNAL)
    
    :param list signature: Signatures to delete
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

    route = "/alarms/v1/signature".format(signature=signature)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

    query_parameters = {}
    # Only send signature if the argument was provided, dont send null values
    if signature is not None:
        query_parameters.update({"signature": signature})
    

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


def get_signatures(
    keywords: str = None,
    keywordField: str = None,
    keywordMatch: str = "all",
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
    """Get all signatures including alarms if mapped (PUBLIC)
    
    :param list keywords: Search by keywords
    :param list keywordField: Set field strategy for keyword search
    :param str keywordMatch: Set match strategy for keyword search
    :param int limit: Maximum number of returned signatures
    :param int offset: Skip a number of signatures
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

    route = "/alarms/v1/signature".format(keywordMatch=keywordMatch,
        limit=limit,
        keywords=keywords,
        keywordField=keywordField,
        offset=offset)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

    query_parameters = {}
    # Only send keywordMatch if the argument was provided, dont send null values
    if keywordMatch is not None:
        query_parameters.update({"keywordMatch": keywordMatch})
    
    # Only send limit if the argument was provided, dont send null values
    if limit is not None:
        query_parameters.update({"limit": limit})
    
    # Only send keywords if the argument was provided, dont send null values
    if keywords is not None:
        query_parameters.update({"keywords": keywords})
    
    # Only send keywordField if the argument was provided, dont send null values
    if keywordField is not None:
        query_parameters.update({"keywordField": keywordField})
    
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


def search_signatures(
    limit: int = None,
    offset: int = None,
    includeDeleted: bool = None,
    includeFlags: int = None,
    excludeFlags: int = None,
    subCriteria: dict = None,
    exclude: bool = None,
    required: bool = None,
    attackCategoryID: int = None,
    alarmID: int = None,
    signature: str = None,
    minTriggerAmount: int = None,
    maxTriggerAmount: int = None,
    startTimestamp: int = None,
    endTimestamp: int = None,
    timeFieldStrategy: str = None,
    timeMatchStrategy: str = None,
    keywords: str = None,
    keywordFieldStrategy: str = None,
    keywordMatchStrategy: str = None,
    sortBy: str = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
) -> dict:
    """Get all signatures matching a given search criteria (PUBLIC)
    
    :param int limit: Set this value to set max number of results. By default\, no restriction on result set size. 
    :param int offset: Set this value to skip the first \(offset\) objects. By default\, return result from first object. 
    :param bool includeDeleted: Set to true to include deleted objects. By default\, exclude deleted objects. 
    :param int includeFlags: Only include objects which have includeFlags set. 
    :param int excludeFlags: Exclude objects which have excludeFlags set. 
    :param list subCriteria: Set additional criterias which are applied using a logical OR. 
    :param bool exclude: Only relevant for subcriteria. If set to true\, objects matching this subcriteria object will be excluded. 
    :param bool required: Only relevant for subcriteria. If set to true\, objects matching this subcriteria are required \(AND\-ed together with parent criteria\). 
    :param list attackCategoryID: A set of IDs for attack categories \(alarm category\). 
    :param list alarmID: A set of IDs for alarms. 
    :param list signature: A set of signatures. It does an exact match. 
    :param int minTriggerAmount: Minimum trigger amount\, default 0 means disabled 
    :param int maxTriggerAmount: Maximum trigger amount\, default 0 means disabled 
    :param int startTimestamp: Only include mappings based on the set TimeFieldStrategy and TimeMatchStrategy \(start timestamp\) 
    :param int endTimestamp: Only include mappings based on the set TimeFieldStrategy and TimeMatchStrategy \(end timestamp\) 
    :param list timeFieldStrategy: TimeFieldStrategy to define which timestamp field\(s\) to match. \(default lastTriggeredTimestamp\)
    :param str timeMatchStrategy: TimeMatchStrategy to define how to match startTimestamp and endTimestamp with fields. \(default any\)
    :param list keywords: A set of keywords matched against mappings based on the set KeywordFieldStrategy and KeywordMatchStrategy. 
    :param list keywordFieldStrategy: KeywordFieldStrategy to define which field\(s\) to match against keywords. \(default all\)
    :param str keywordMatchStrategy: KeywordMatchStrategy to define how to match keywords with fields. \(default all\)
    :param list sortBy: List of properties to sort by \(prefix with \"\-\" to sort descending\). 
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

    route = "/alarms/v1/signature/search".format()

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}
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
    # Only send attackCategoryID if the argument was provided, dont send null values
    if attackCategoryID is not None:
        body.update({"attackCategoryID": attackCategoryID})
    # Only send alarmID if the argument was provided, dont send null values
    if alarmID is not None:
        body.update({"alarmID": alarmID})
    # Only send signature if the argument was provided, dont send null values
    if signature is not None:
        body.update({"signature": signature})
    # Only send minTriggerAmount if the argument was provided, dont send null values
    if minTriggerAmount is not None:
        body.update({"minTriggerAmount": minTriggerAmount})
    # Only send maxTriggerAmount if the argument was provided, dont send null values
    if maxTriggerAmount is not None:
        body.update({"maxTriggerAmount": maxTriggerAmount})
    # Only send startTimestamp if the argument was provided, dont send null values
    if startTimestamp is not None:
        body.update({"startTimestamp": startTimestamp})
    # Only send endTimestamp if the argument was provided, dont send null values
    if endTimestamp is not None:
        body.update({"endTimestamp": endTimestamp})
    # Only send timeFieldStrategy if the argument was provided, dont send null values
    if timeFieldStrategy is not None:
        body.update({"timeFieldStrategy": timeFieldStrategy})
    # Only send timeMatchStrategy if the argument was provided, dont send null values
    if timeMatchStrategy is not None:
        body.update({"timeMatchStrategy": timeMatchStrategy})
    # Only send keywords if the argument was provided, dont send null values
    if keywords is not None:
        body.update({"keywords": keywords})
    # Only send keywordFieldStrategy if the argument was provided, dont send null values
    if keywordFieldStrategy is not None:
        body.update({"keywordFieldStrategy": keywordFieldStrategy})
    # Only send keywordMatchStrategy if the argument was provided, dont send null values
    if keywordMatchStrategy is not None:
        body.update({"keywordMatchStrategy": keywordMatchStrategy})
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
