"""Autogenerated API"""
from argus_api import session


def aggregate_metrics(
    descriptor: str,
    descriptorDomain: str = None,
    customer: str = None,
    customerDomain: str = None,
    keys: dict = None,
    subCriteria: dict = None,
    startTimestamp: int = None,
    endTimestamp: int = None,
    resolution: int = None,
    resolutionUnit: str = None,
    groupBy: dict = None,
    calendarInterval: str = None,
    values: dict = None,
    groupByCustomer: bool = None,
    includeOthers: bool = True,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
) -> dict:
    """Fetch metrics that matches given aggregation criteria (DEV)
    
    :param str descriptor: Shortname or ID of descriptor
    :param str descriptorDomain: Domain which is used if short name is specified for \'descriptor\' parameter. Defaults to current user domain.
    :param list customer: Restrict result set to records bound to specified customers. The list accepts both ID or shortname for the customers. For global metrics\, this field should not be set. 
    :param str customerDomain: Restrict result set to records with customers from the specific domain. The field accepts ID or shortname for the domain. 
    :param dict keys: Restrict result set to records with these key names and key values. Must match the keys given in the descriptor\, but IP type allows using IP ranges\, such as 192.168.0.0\/16 for IPv4 or 2001\:db8\:\:\/48 for IPv6. 
    :param list subCriteria: Set additional criterias to be applied as specified in the subcriteria object\(s\) \(AND\, AND NOT\, OR\). \(default OR\)
    :param int startTimestamp: Restrict result set to records submitted after this timestamp. Accepts ISO\-8601 timestamp string. 
    :param int endTimestamp: Restrict result set to records submitted before this timestamp. Accepts ISO\-8601 timestamp string. \(default now\)
    :param int resolution: Aggregation resolution period in units specified by \'resolutionUnit\' property. If 0 the resolution is the entire time span given by the start and end timestamps. If the expected combination of timestamps\, resolution\, and resolution unit would result in more buckets than ElasticSearch permits\, which is 10000\, then the request will be denied. Note that the initial calculation on this is rough\, and that ES might still deny the request. In which case lower the resolution. 
    :param str resolutionUnit: Units for aggregation resolution. \(default millisecond\)
    :param list groupBy: List of descriptor\'s key names for aggregating the result. The result will be grouped into key buckets up to the limit given.The buckets themselves will be ordered in a descending order based on the values aggregated. 
    :param str calendarInterval: States the calendar interval the aggregation results should be sorted by\, such as month or year.It only allows for a resolution of 1\, and overrides the resolution unit such that if calendar interval is week\, then the result will be in intervals of 1 whole week\, expanding backwards in time for start and forwards for end. It is by defaults not used and set to null. \(default null\)
    :param list values: Descriptor\'s values included in aggregation result. 
    :param bool groupByCustomer: States whether Metric records will be aggregated by customers. It defaults to false. \(default false\)
    :param bool includeOthers: States whether the aggregation results will contain buckets for the data not included in the keys given by the groupBy field.Is not used if the groupBy field is empty. It defaults to true. \(default true\)
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
    :raises ValidationFailedException: on 412
    :raises ArgusException: on other status codes
    
    :returns: dictionary translated from JSON
    """

    route = "/metrics/v1/metric/{descriptor}/aggregate".format(descriptor=descriptor,
        descriptorDomain=descriptorDomain)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}
    # Only send customer if the argument was provided, dont send null values
    if customer is not None:
        body.update({"customer": customer})
    # Only send customerDomain if the argument was provided, dont send null values
    if customerDomain is not None:
        body.update({"customerDomain": customerDomain})
    # Only send keys if the argument was provided, dont send null values
    if keys is not None:
        body.update({"keys": keys})
    # Only send subCriteria if the argument was provided, dont send null values
    if subCriteria is not None:
        body.update({"subCriteria": subCriteria})
    # Only send startTimestamp if the argument was provided, dont send null values
    if startTimestamp is not None:
        body.update({"startTimestamp": startTimestamp})
    # Only send endTimestamp if the argument was provided, dont send null values
    if endTimestamp is not None:
        body.update({"endTimestamp": endTimestamp})
    # Only send resolution if the argument was provided, dont send null values
    if resolution is not None:
        body.update({"resolution": resolution})
    # Only send resolutionUnit if the argument was provided, dont send null values
    if resolutionUnit is not None:
        body.update({"resolutionUnit": resolutionUnit})
    # Only send groupBy if the argument was provided, dont send null values
    if groupBy is not None:
        body.update({"groupBy": groupBy})
    # Only send groupByCustomer if the argument was provided, dont send null values
    if groupByCustomer is not None:
        body.update({"groupByCustomer": groupByCustomer})
    # Only send includeOthers if the argument was provided, dont send null values
    if includeOthers is not None:
        body.update({"includeOthers": includeOthers})
    # Only send calendarInterval if the argument was provided, dont send null values
    if calendarInterval is not None:
        body.update({"calendarInterval": calendarInterval})
    # Only send values if the argument was provided, dont send null values
    if values is not None:
        body.update({"values": values})

    query_parameters = {}
    # Only send descriptorDomain if the argument was provided, dont send null values
    if descriptorDomain is not None:
        query_parameters.update({"descriptorDomain": descriptorDomain})
    

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


def search_metrics(
    descriptor: str,
    descriptorDomain: str = None,
    customer: str = None,
    customerDomain: str = None,
    keys: dict = None,
    subCriteria: dict = None,
    startTimestamp: int = None,
    endTimestamp: int = None,
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
    """Search the submitted metrics for a specific descriptor. (DEV)
    
    :param str descriptor: Shortname or ID of descriptor
    :param str descriptorDomain: Domain which is used if short name is specified for \'descriptor\' parameter. Defaults to current user domain.
    :param list customer: Restrict result set to records bound to specified customers. The list accepts both ID or shortname for the customers. For global metrics\, this field should not be set. 
    :param str customerDomain: Restrict result set to records with customers from the specific domain. The field accepts ID or shortname for the domain. 
    :param dict keys: Restrict result set to records with these key names and key values. Must match the keys given in the descriptor\, but IP type allows using IP ranges\, such as 192.168.0.0\/16 for IPv4 or 2001\:db8\:\:\/48 for IPv6. 
    :param list subCriteria: Set additional criterias to be applied as specified in the subcriteria object\(s\) \(AND\, AND NOT\, OR\). \(default OR\)
    :param int startTimestamp: Restrict result set to records submitted after this timestamp. Accepts ISO\-8601 timestamp string. 
    :param int endTimestamp: Restrict result set to records submitted before this timestamp. Accepts ISO\-8601 timestamp string. \(default now\)
    :param int offset: Set this value to skip the first \(offset\) objects. By default\, return result from first object.Cannot\, in combination with the limit\, exceed 10000\, as this will exceed the Elasticsearch search window. 
    :param int limit: Set this value to set max number of results. Cannot exceed 10000 which is the Elasticsearch search window. \(default 25\)
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
    :raises ValidationFailedException: on 412
    :raises ArgusException: on other status codes
    
    :returns: dictionary translated from JSON
    """

    route = "/metrics/v1/metric/{descriptor}/search".format(descriptor=descriptor,
        descriptorDomain=descriptorDomain)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}
    # Only send customer if the argument was provided, dont send null values
    if customer is not None:
        body.update({"customer": customer})
    # Only send customerDomain if the argument was provided, dont send null values
    if customerDomain is not None:
        body.update({"customerDomain": customerDomain})
    # Only send keys if the argument was provided, dont send null values
    if keys is not None:
        body.update({"keys": keys})
    # Only send subCriteria if the argument was provided, dont send null values
    if subCriteria is not None:
        body.update({"subCriteria": subCriteria})
    # Only send startTimestamp if the argument was provided, dont send null values
    if startTimestamp is not None:
        body.update({"startTimestamp": startTimestamp})
    # Only send endTimestamp if the argument was provided, dont send null values
    if endTimestamp is not None:
        body.update({"endTimestamp": endTimestamp})
    # Only send limit if the argument was provided, dont send null values
    if limit is not None:
        body.update({"limit": limit})
    # Only send offset if the argument was provided, dont send null values
    if offset is not None:
        body.update({"offset": offset})

    query_parameters = {}
    # Only send descriptorDomain if the argument was provided, dont send null values
    if descriptorDomain is not None:
        query_parameters.update({"descriptorDomain": descriptorDomain})
    

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


def submit_metric(
    descriptor: str,
    descriptorDomain: str = None,
    records: dict = None,
    ignoreOnFailed: bool = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
) -> dict:
    """Submit new metric (DEV)
    
    :param str descriptor: ID or short name of metric descriptor
    :param str descriptorDomain: Domain which is used if short name is specified for \'descriptor\' parameter. Defaults to current user domain.
    :param list records: Metric records for submission. 
    :param bool ignoreOnFailed: Set this value for successful response even failures occur while submitting. \(default false\)
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
    :raises ValidationFailedException: on 412
    :raises ArgusException: on other status codes
    
    :returns: dictionary translated from JSON
    """

    route = "/metrics/v1/metric/{descriptor}".format(descriptor=descriptor,
        descriptorDomain=descriptorDomain)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}
    # Only send records if the argument was provided, dont send null values
    if records is not None:
        body.update({"records": records})
    # Only send ignoreOnFailed if the argument was provided, dont send null values
    if ignoreOnFailed is not None:
        body.update({"ignoreOnFailed": ignoreOnFailed})

    query_parameters = {}
    # Only send descriptorDomain if the argument was provided, dont send null values
    if descriptorDomain is not None:
        query_parameters.update({"descriptorDomain": descriptorDomain})
    

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
