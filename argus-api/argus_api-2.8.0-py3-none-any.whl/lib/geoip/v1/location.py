"""Autogenerated API"""
from argus_api import session


def add_location(
    id: int = None,
    extID: int = None,
    countryCode: str = None,
    regionCode: str = None,
    cityName: str = None,
    postalCode: str = None,
    metroCode: str = None,
    areaCode: str = None,
    lastModified: int = None,
    flags: int = None,
    latitude: float = None,
    longitude: float = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
) -> dict:
    """Add new location (DEV)
    
    :param int id: 
    :param int extID: 
    :param str countryCode: 
    :param str regionCode: 
    :param str cityName: 
    :param str postalCode: 
    :param str metroCode: 
    :param str areaCode: 
    :param int lastModified: 
    :param int flags: 
    :param float latitude: 
    :param float longitude: 
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

    route = "/geoip/v1/location".format()

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}
    # Only send id if the argument was provided, dont send null values
    if id is not None:
        body.update({"id": id})
    # Only send extID if the argument was provided, dont send null values
    if extID is not None:
        body.update({"extID": extID})
    # Only send countryCode if the argument was provided, dont send null values
    if countryCode is not None:
        body.update({"countryCode": countryCode})
    # Only send regionCode if the argument was provided, dont send null values
    if regionCode is not None:
        body.update({"regionCode": regionCode})
    # Only send cityName if the argument was provided, dont send null values
    if cityName is not None:
        body.update({"cityName": cityName})
    # Only send postalCode if the argument was provided, dont send null values
    if postalCode is not None:
        body.update({"postalCode": postalCode})
    # Only send metroCode if the argument was provided, dont send null values
    if metroCode is not None:
        body.update({"metroCode": metroCode})
    # Only send areaCode if the argument was provided, dont send null values
    if areaCode is not None:
        body.update({"areaCode": areaCode})
    # Only send lastModified if the argument was provided, dont send null values
    if lastModified is not None:
        body.update({"lastModified": lastModified})
    # Only send flags if the argument was provided, dont send null values
    if flags is not None:
        body.update({"flags": flags})
    # Only send latitude if the argument was provided, dont send null values
    if latitude is not None:
        body.update({"latitude": latitude})
    # Only send longitude if the argument was provided, dont send null values
    if longitude is not None:
        body.update({"longitude": longitude})

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


def get_location(
    id: int,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
) -> dict:
    """Lookup location (DEV)
    
    :param int id: Location ID
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

    route = "/geoip/v1/location/{id}".format(id=id)

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
