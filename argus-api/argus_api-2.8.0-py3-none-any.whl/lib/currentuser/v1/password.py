"""Autogenerated API"""
from argus_api import session
from argus_api.utils import deprecated_alias


def change_password(
    oldPassword: str = None,
    newPassword: str = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
) -> dict:
    """Change current users Argus password. Note that this will only change the password used for SMS, PASSWORD and TOTP, not external authentications like LDAP or RADIUS. (PUBLIC)
    
    :param str oldPassword: Existing password\, to validate password change
    :param str newPassword: New password to change to.
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
    :raises InvalidPasswordException: on 412
    :raises ArgusException: on other status codes
    
    :returns: dictionary translated from JSON
    """

    route = "/currentuser/v1/password".format()

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}
    # Only send oldPassword if the argument was provided, dont send null values
    if oldPassword is not None:
        body.update({"oldPassword": oldPassword})
    # Only send newPassword if the argument was provided, dont send null values
    if newPassword is not None:
        body.update({"newPassword": newPassword})

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

#: **DEPRECATED** : ``set_properties`` is an alias for ``change_password``. Exists
#: only for backward compatibility - **do not use** - use ``change_password`` instead.
set_properties = deprecated_alias("set_properties")(change_password)