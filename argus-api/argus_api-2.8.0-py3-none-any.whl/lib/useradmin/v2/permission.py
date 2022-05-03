"""Autogenerated API"""
from argus_api import session


def grant_permission(
    subject: str = None,
    customer: str = None,
    function: str = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
) -> dict:
    """Grants a permission to a user (PUBLIC)
    
    :param str subject: Subject to grant the function to \(id or name\)
    :param str customer: Customer that the function is valid for \(id or name\)
    :param str function: Function to grant \(id or name\)
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

    route = "/useradmin/v2/permission".format()

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}
    # Only send subject if the argument was provided, dont send null values
    if subject is not None:
        body.update({"subject": subject})
    # Only send customer if the argument was provided, dont send null values
    if customer is not None:
        body.update({"customer": customer})
    # Only send function if the argument was provided, dont send null values
    if function is not None:
        body.update({"function": function})

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


def list_permissions(
    domain: str = None,
    subject: str = None,
    customer: str = None,
    function: str = None,
    keywords: str = None,
    keywordField: str = None,
    limit: int = 25,
    includeSubjectAscendants: bool = True,
    includeSubjectDescendants: bool = True,
    includeCustomerAscendants: bool = True,
    includeCustomerDescendants: bool = True,
    includeFunctionAscendants: bool = True,
    includeFunctionDescendants: bool = True,
    keywordMatch: str = "all",
    offset: int = None,
    includeDeleted: bool = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
) -> dict:
    """Searches for permissions, defaults to showing all permissions (PUBLIC)
    
    :param str domain: Name or ID of the domain to search
    :param list subject: Name or ID of the subject
    :param list customer: Name or ID of the customer
    :param list function: Name or ID of the function
    :param list keywords: Search by keywords
    :param list keywordField: Set field strategy for keyword search
    :param int limit: Maximum number of returned results
    :param bool includeSubjectAscendants: Include permissions for ascending subjects
    :param bool includeSubjectDescendants: Include permissions for descending subjects
    :param bool includeCustomerAscendants: Include permissions for ascending customers
    :param bool includeCustomerDescendants: Include permissions for descending customers
    :param bool includeFunctionAscendants: Include permissions for ascending functions
    :param bool includeFunctionDescendants: Include permissions for descending functions
    :param str keywordMatch: Set match strategy for keyword search
    :param int offset: Skip a number of results
    :param bool includeDeleted: Include deleted permissions
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

    route = "/useradmin/v2/permission".format(limit=limit,
        includeSubjectAscendants=includeSubjectAscendants,
        includeSubjectDescendants=includeSubjectDescendants,
        includeCustomerAscendants=includeCustomerAscendants,
        includeCustomerDescendants=includeCustomerDescendants,
        includeFunctionAscendants=includeFunctionAscendants,
        includeFunctionDescendants=includeFunctionDescendants,
        keywordMatch=keywordMatch,
        offset=offset,
        domain=domain,
        subject=subject,
        customer=customer,
        function=function,
        keywords=keywords,
        keywordField=keywordField,
        includeDeleted=includeDeleted)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

    query_parameters = {}
    # Only send limit if the argument was provided, dont send null values
    if limit is not None:
        query_parameters.update({"limit": limit})
    
    # Only send includeSubjectAscendants if the argument was provided, dont send null values
    if includeSubjectAscendants is not None:
        query_parameters.update({"includeSubjectAscendants": includeSubjectAscendants})
    
    # Only send includeSubjectDescendants if the argument was provided, dont send null values
    if includeSubjectDescendants is not None:
        query_parameters.update({"includeSubjectDescendants": includeSubjectDescendants})
    
    # Only send includeCustomerAscendants if the argument was provided, dont send null values
    if includeCustomerAscendants is not None:
        query_parameters.update({"includeCustomerAscendants": includeCustomerAscendants})
    
    # Only send includeCustomerDescendants if the argument was provided, dont send null values
    if includeCustomerDescendants is not None:
        query_parameters.update({"includeCustomerDescendants": includeCustomerDescendants})
    
    # Only send includeFunctionAscendants if the argument was provided, dont send null values
    if includeFunctionAscendants is not None:
        query_parameters.update({"includeFunctionAscendants": includeFunctionAscendants})
    
    # Only send includeFunctionDescendants if the argument was provided, dont send null values
    if includeFunctionDescendants is not None:
        query_parameters.update({"includeFunctionDescendants": includeFunctionDescendants})
    
    # Only send keywordMatch if the argument was provided, dont send null values
    if keywordMatch is not None:
        query_parameters.update({"keywordMatch": keywordMatch})
    
    # Only send offset if the argument was provided, dont send null values
    if offset is not None:
        query_parameters.update({"offset": offset})
    
    # Only send domain if the argument was provided, dont send null values
    if domain is not None:
        query_parameters.update({"domain": domain})
    
    # Only send subject if the argument was provided, dont send null values
    if subject is not None:
        query_parameters.update({"subject": subject})
    
    # Only send customer if the argument was provided, dont send null values
    if customer is not None:
        query_parameters.update({"customer": customer})
    
    # Only send function if the argument was provided, dont send null values
    if function is not None:
        query_parameters.update({"function": function})
    
    # Only send keywords if the argument was provided, dont send null values
    if keywords is not None:
        query_parameters.update({"keywords": keywords})
    
    # Only send keywordField if the argument was provided, dont send null values
    if keywordField is not None:
        query_parameters.update({"keywordField": keywordField})
    
    # Only send includeDeleted if the argument was provided, dont send null values
    if includeDeleted is not None:
        query_parameters.update({"includeDeleted": includeDeleted})
    

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


def revoke_permission(
    permissionID: int,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
) -> dict:
    """Revokes a permission from a user (PUBLIC)
    
    :param int permissionID: ID of permission
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

    route = "/useradmin/v2/permission/{permissionID}".format(permissionID=permissionID)

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


def search_permissions(
    subCriteria: dict = None,
    keywordMatchStrategy: str = None,
    keywords: str = None,
    keywordFieldStrategy: str = None,
    startTimestamp: str = None,
    endTimestamp: str = None,
    timeMatchStrategy: str = None,
    timeFieldStrategy: str = None,
    subject: str = None,
    customer: str = None,
    function: str = None,
    domain: str = None,
    sortBy: str = None,
    includeSubjectAscendants: bool = True,
    includeSubjectDescendants: bool = True,
    includeCustomerAscendants: bool = True,
    includeCustomerDescendants: bool = True,
    includeFunctionAscendants: bool = True,
    includeFunctionDescendants: bool = True,
    includeDeleted: bool = None,
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
    """Searches for permissions, defaults to showing all permissions (PUBLIC)
    
    :param list subCriteria: 
    :param str keywordMatchStrategy: Search based on all keywords \(AND\)\, or based on any keyword \(OR\) \(default Match all keywords \(AND\)\)
    :param list keywords: Keywords to search for
    :param list keywordFieldStrategy: Which fields will be searched for the given keyword \(default All supported fields\)
    :param str startTimestamp: Restrict search to data after this time \(epoch millis\) according to selected TimeFieldStrategies. Allows unix timestamp \(milliseconds\)\, ISO timestamp\, or relative time specifies. See https\:\/\/docs.mnemonic.no\/x\/AQDXAQ
    :param str endTimestamp: Restrict search to data before this time \(epoch millis\) according to selected TimeFieldStrategies. Allows unix timestamp \(milliseconds\)\, ISO timestamp\, or relative time specifies. See https\:\/\/docs.mnemonic.no\/x\/AQDXAQ
    :param str timeMatchStrategy: Specify if the specified time period must match all the searched time fields\, or if it will match for any field. Default is any.
    :param list timeFieldStrategy: Determine fields to search for by time \(defaults to all\)
    :param list subject: The ID or shortname of subjects to search for
    :param list customer: The ID or shortname of customers to search for
    :param list function: The ID or shortname of functions to search for
    :param str domain: The ID or shortname of the domain where the subjects and customers are located
    :param list sortBy: Field to sort result by \(will sort by the fields ID\, not name\) \(default subject\)
    :param bool includeSubjectAscendants: Incude permissions given for subject ascendants \(default true\)
    :param bool includeSubjectDescendants: Incude permissions given for subject descendants \(default true\)
    :param bool includeCustomerAscendants: Incude permissions given for customer ascendants \(default true\)
    :param bool includeCustomerDescendants: Incude permissions given for customer descendants \(default true\)
    :param bool includeFunctionAscendants: Incude permissions given for function ascendants \(default true\)
    :param bool includeFunctionDescendants: Incude permissions given for function descendants \(default true\)
    :param bool includeDeleted: Include deleted permissions \(default false\)
    :param int limit: The max amount of items to display \(default 25\)
    :param int offset: The amount of items to skip \(default 0\)
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

    route = "/useradmin/v2/permission/search".format()

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}
    # Only send subCriteria if the argument was provided, dont send null values
    if subCriteria is not None:
        body.update({"subCriteria": subCriteria})
    # Only send keywordMatchStrategy if the argument was provided, dont send null values
    if keywordMatchStrategy is not None:
        body.update({"keywordMatchStrategy": keywordMatchStrategy})
    # Only send keywords if the argument was provided, dont send null values
    if keywords is not None:
        body.update({"keywords": keywords})
    # Only send keywordFieldStrategy if the argument was provided, dont send null values
    if keywordFieldStrategy is not None:
        body.update({"keywordFieldStrategy": keywordFieldStrategy})
    # Only send startTimestamp if the argument was provided, dont send null values
    if startTimestamp is not None:
        body.update({"startTimestamp": startTimestamp})
    # Only send endTimestamp if the argument was provided, dont send null values
    if endTimestamp is not None:
        body.update({"endTimestamp": endTimestamp})
    # Only send timeMatchStrategy if the argument was provided, dont send null values
    if timeMatchStrategy is not None:
        body.update({"timeMatchStrategy": timeMatchStrategy})
    # Only send timeFieldStrategy if the argument was provided, dont send null values
    if timeFieldStrategy is not None:
        body.update({"timeFieldStrategy": timeFieldStrategy})
    # Only send subject if the argument was provided, dont send null values
    if subject is not None:
        body.update({"subject": subject})
    # Only send customer if the argument was provided, dont send null values
    if customer is not None:
        body.update({"customer": customer})
    # Only send function if the argument was provided, dont send null values
    if function is not None:
        body.update({"function": function})
    # Only send domain if the argument was provided, dont send null values
    if domain is not None:
        body.update({"domain": domain})
    # Only send sortBy if the argument was provided, dont send null values
    if sortBy is not None:
        body.update({"sortBy": sortBy})
    # Only send includeSubjectAscendants if the argument was provided, dont send null values
    if includeSubjectAscendants is not None:
        body.update({"includeSubjectAscendants": includeSubjectAscendants})
    # Only send includeSubjectDescendants if the argument was provided, dont send null values
    if includeSubjectDescendants is not None:
        body.update({"includeSubjectDescendants": includeSubjectDescendants})
    # Only send includeCustomerAscendants if the argument was provided, dont send null values
    if includeCustomerAscendants is not None:
        body.update({"includeCustomerAscendants": includeCustomerAscendants})
    # Only send includeCustomerDescendants if the argument was provided, dont send null values
    if includeCustomerDescendants is not None:
        body.update({"includeCustomerDescendants": includeCustomerDescendants})
    # Only send includeFunctionAscendants if the argument was provided, dont send null values
    if includeFunctionAscendants is not None:
        body.update({"includeFunctionAscendants": includeFunctionAscendants})
    # Only send includeFunctionDescendants if the argument was provided, dont send null values
    if includeFunctionDescendants is not None:
        body.update({"includeFunctionDescendants": includeFunctionDescendants})
    # Only send includeDeleted if the argument was provided, dont send null values
    if includeDeleted is not None:
        body.update({"includeDeleted": includeDeleted})
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
