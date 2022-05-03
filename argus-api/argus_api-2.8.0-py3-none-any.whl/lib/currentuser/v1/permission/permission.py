"""Autogenerated API"""
from argus_api import session


def check_permission(
    function: str,
    customerID: str,
    domain: str = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
) -> dict:
    """Validate current user permission to perform function on specific customer (PUBLIC)
    
    :param str function: Function name
    :param str customerID: Customer ID or shortname
    :param str domain: Domain ID or shortname for domain to lookup customer by shortname. Defaults to current users domain
    :param json: return the response's body as a ``dict`` parsed from json. ``True`` by
      default. If set to false, the raw ``requests.Response`` object will be returned.
    :param verify: path to a certificate bundle or boolean indicating whether SSL
      verification should be performed.
    :param apiKey: Argus API key.
    :param authentication: authentication override
    :param server_url: API base URL override
    :param body: body of the request. other parameters will override keys defined in the body.
    :raises AuthenticationFailedException: on 401
    :raises ForbiddenPermissionException: on 403
    :raises UserNotFoundException: on 404
    :raises ValidationFailedException: on 412
    :raises ArgusException: on other status codes
    
    :returns: dictionary translated from JSON
    """

    route = "/currentuser/v1/permission/{function}/{customer}".format(function=function,
        customer=customerID,
        domain=domain)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

    query_parameters = {}
    # Only send domain if the argument was provided, dont send null values
    if domain is not None:
        query_parameters.update({"domain": domain})
    

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
