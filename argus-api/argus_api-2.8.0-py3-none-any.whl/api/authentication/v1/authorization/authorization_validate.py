"""Autogenerated API"""
from argus_api import session
import logging
from argus_cli.plugin import register_command
from argus_plugins import argus_cli_module
log = logging.getLogger(__name__)


@register_command(
    extending=("authentication", "v1", "authorization", "validate"),
    module=argus_cli_module
)
def validate_user_authorization(
    operation: str = None,
    context: dict = None,
    authorization: str = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
) -> dict:
    """Validate authorization token (PUBLIC)
    
    :param str operation: The name of the operation
    :param dict context: Context variables to scope this authorization. All context variables must be present in the authorization token and their value must be equal to those provided here.
    :param str authorization: The authorization JWT token
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

    route = "/authentication/v1/authorization/validate".format()

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
    # Only send authorization if the argument was provided, dont send null values
    if authorization is not None:
        body.update({"authorization": authorization})

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
