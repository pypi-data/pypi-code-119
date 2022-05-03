"""Autogenerated API"""
from argus_api import session
import logging
from argus_cli.plugin import register_command
from argus_plugins import argus_cli_module
log = logging.getLogger(__name__)


@register_command(
    extending=("currentuser", "v1", "groups"),
    module=argus_cli_module
)
def get_current_user_groups(
    limit: int = 25,
    includeAncestors: bool = None,
    offset: int = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
) -> dict:
    """Get list of groups which current user is a member of. Result will be sorted by id (ascending) (PUBLIC)
    
    :param int limit: Maximum number of values to return
    :param bool includeAncestors: If true\, also include group ancestors
    :param int offset: Skip this number of records
    :param json: return the response's body as a ``dict`` parsed from json. ``True`` by
      default. If set to false, the raw ``requests.Response`` object will be returned.
    :param verify: path to a certificate bundle or boolean indicating whether SSL
      verification should be performed.
    :param apiKey: Argus API key.
    :param authentication: authentication override
    :param server_url: API base URL override
    :param body: body of the request. other parameters will override keys defined in the body.
    :raises AuthenticationFailedException: on 401
    :raises ArgusException: on other status codes
    
    :returns: dictionary translated from JSON
    """

    route = "/currentuser/v1/groups".format(limit=limit,
        includeAncestors=includeAncestors,
        offset=offset)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

    query_parameters = {}
    # Only send limit if the argument was provided, dont send null values
    if limit is not None:
        query_parameters.update({"limit": limit})
    
    # Only send includeAncestors if the argument was provided, dont send null values
    if includeAncestors is not None:
        query_parameters.update({"includeAncestors": includeAncestors})
    
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
