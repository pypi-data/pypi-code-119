"""Autogenerated API"""
from argus_api import session
from argus_api.utils import deprecated_alias


def ldap_authentication(
    requestedAuthorizations: str = None,
    userName: str = None,
    domain: str = None,
    password: str = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
) -> dict:
    """Initiate a new user session using LDAP authentication (PUBLIC)
    
    :param list requestedAuthorizations: Allow client to request authorizations as part of the authentication transaction. The client is not guaranteed to get the requested authorizations. The setPassword authorization is only returned if the current user has the FORCE\_PW\_CHANGE flag set.
    :param str userName: Username to authenticate
    :param str domain: User domain
    :param str password: LDAP password for user
    :param json: return the response's body as a ``dict`` parsed from json. ``True`` by
      default. If set to false, the raw ``requests.Response`` object will be returned.
    :param verify: path to a certificate bundle or boolean indicating whether SSL
      verification should be performed.
    :param apiKey: Argus API key.
    :param authentication: authentication override
    :param server_url: API base URL override
    :param body: body of the request. other parameters will override keys defined in the body.
    :raises AuthenticationFailedException: on 401
    :raises ValidationErrorException: on 412
    :raises ArgusException: on other status codes
    
    :returns: dictionary translated from JSON
    """

    route = "/authentication/v1/ldap/authentication".format()

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}
    # Only send requestedAuthorizations if the argument was provided, dont send null values
    if requestedAuthorizations is not None:
        body.update({"requestedAuthorizations": requestedAuthorizations})
    # Only send userName if the argument was provided, dont send null values
    if userName is not None:
        body.update({"userName": userName})
    # Only send domain if the argument was provided, dont send null values
    if domain is not None:
        body.update({"domain": domain})
    # Only send password if the argument was provided, dont send null values
    if password is not None:
        body.update({"password": password})

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


def ldap_user_authorization(
    operation: str = None,
    context: dict = None,
    nextURI: str = None,
    password: str = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
) -> dict:
    """Request an authorization token using LDAP credentials (INTERNAL)
    
    :param str operation: The name of the operation to authorize
    :param dict context: Context variables to scope this authorization. All context variables required by the executing service must be present and equal to those provided here.
    :param str nextURI: The URI to redirect\/route to after successful authorization. The URI will be validated according to policy. The authorization token returned from successful authorization should be appended as a query parameter to this URI.
    :param str password: The current users LDAP password
    :param json: return the response's body as a ``dict`` parsed from json. ``True`` by
      default. If set to false, the raw ``requests.Response`` object will be returned.
    :param verify: path to a certificate bundle or boolean indicating whether SSL
      verification should be performed.
    :param apiKey: Argus API key.
    :param authentication: authentication override
    :param server_url: API base URL override
    :param body: body of the request. other parameters will override keys defined in the body.
    :raises AuthenticationFailedException: on 401
    :raises ValidationErrorException: on 412
    :raises ArgusException: on other status codes
    
    :returns: dictionary translated from JSON
    """

    route = "/authentication/v1/ldap/authorize".format()

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}
    # Only send operation if the argument was provided, dont send null values
    if operation is not None:
        body.update({"operation": operation})
    # Only send context if the argument was provided, dont send null values
    if context is not None:
        body.update({"context": context})
    # Only send nextURI if the argument was provided, dont send null values
    if nextURI is not None:
        body.update({"nextURI": nextURI})
    # Only send password if the argument was provided, dont send null values
    if password is not None:
        body.update({"password": password})

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


def legacy_ldap_authentication(
    requestedAuthorizations: str = None,
    userName: str = None,
    domain: str = None,
    password: str = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
) -> dict:
    """Initiate a new user session using LDAP authentication (PUBLIC)
    
    :param list requestedAuthorizations: Allow client to request authorizations as part of the authentication transaction. The client is not guaranteed to get the requested authorizations. The setPassword authorization is only returned if the current user has the FORCE\_PW\_CHANGE flag set.
    :param str userName: Username to authenticate
    :param str domain: User domain
    :param str password: LDAP password for user
    :param json: return the response's body as a ``dict`` parsed from json. ``True`` by
      default. If set to false, the raw ``requests.Response`` object will be returned.
    :param verify: path to a certificate bundle or boolean indicating whether SSL
      verification should be performed.
    :param apiKey: Argus API key.
    :param authentication: authentication override
    :param server_url: API base URL override
    :param body: body of the request. other parameters will override keys defined in the body.
    :raises AuthenticationFailedException: on 401
    :raises ValidationErrorException: on 412
    :raises ArgusException: on other status codes
    
    :returns: dictionary translated from JSON
    """

    route = "/authentication/v1/ldap/authenticate".format()

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}
    # Only send requestedAuthorizations if the argument was provided, dont send null values
    if requestedAuthorizations is not None:
        body.update({"requestedAuthorizations": requestedAuthorizations})
    # Only send userName if the argument was provided, dont send null values
    if userName is not None:
        body.update({"userName": userName})
    # Only send domain if the argument was provided, dont send null values
    if domain is not None:
        body.update({"domain": domain})
    # Only send password if the argument was provided, dont send null values
    if password is not None:
        body.update({"password": password})

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

#: **DEPRECATED** : ``legacy_l_d_a_p_authentication`` is an alias for ``legacy_ldap_authentication``. Exists
#: only for backward compatibility - **do not use** - use ``legacy_ldap_authentication`` instead.
legacy_l_d_a_p_authentication = deprecated_alias("legacy_l_d_a_p_authentication")(legacy_ldap_authentication)