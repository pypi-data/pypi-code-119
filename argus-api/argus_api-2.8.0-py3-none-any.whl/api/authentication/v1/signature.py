"""Autogenerated API"""
from argus_api import session
import logging
from argus_cli.plugin import register_command
from argus_plugins import argus_cli_module
from argus_api.utils import deprecated_alias
log = logging.getLogger(__name__)


@register_command(
    extending=("authentication", "v1", "signature"),
    module=argus_cli_module
)
def enroll_public_key(
    challengeID: str = None,
    type: str = None,
    algorithm: str = None,
    name: str = None,
    publicKey: str = None,
    attestationObject: str = None,
    clientData: str = None,
    authorization: str = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
) -> dict:
    """Enroll new public key (PUBLIC)
    
    :param str challengeID: ID of the challenge this request is bound to
    :param str type: The type of the key
    :param str algorithm: The key algorithm
    :param str name: A name to associate with the key
    :param str publicKey: The key material
    :param str attestationObject: The attestation object \(expected format depends on type\)
    :param str clientData: The clientData which is attested \(expected format depends on type\)
    :param str authorization: The authorization token to permit enrolling this key. Token must be valid for operation \'publickey.enroll\'
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

    route = "/authentication/v1/signature/enroll".format()

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}
    # Only send challengeID if the argument was provided, dont send null values
    if challengeID is not None:
        body.update({"challengeID": challengeID})
    # Only send type if the argument was provided, dont send null values
    if type is not None:
        body.update({"type": type})
    # Only send algorithm if the argument was provided, dont send null values
    if algorithm is not None:
        body.update({"algorithm": algorithm})
    # Only send name if the argument was provided, dont send null values
    if name is not None:
        body.update({"name": name})
    # Only send publicKey if the argument was provided, dont send null values
    if publicKey is not None:
        body.update({"publicKey": publicKey})
    # Only send attestationObject if the argument was provided, dont send null values
    if attestationObject is not None:
        body.update({"attestationObject": attestationObject})
    # Only send clientData if the argument was provided, dont send null values
    if clientData is not None:
        body.update({"clientData": clientData})
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

@register_command(
    extending=("authentication", "v1", "signature"),
    module=argus_cli_module
)
def enroll_webauthn_key(
    challengeID: str = None,
    webAuthnKeyID: str = None,
    attestationObject: str = None,
    clientData: str = None,
    authorization: str = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
) -> dict:
    """Enroll new webauthn key (PUBLIC)
    
    :param str challengeID: ID of the challenge this request is bound to
    :param str webAuthnKeyID: The WebAuthn keyID
    :param str attestationObject: The WebAuthn attestation object
    :param str clientData: The WebAuthn clientData which is attested
    :param str authorization: The authorization token to permit enrolling this key. Token must be valid for operation \'publickey.enroll\'
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

    route = "/authentication/v1/signature/webauthn/enroll".format()

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}
    # Only send challengeID if the argument was provided, dont send null values
    if challengeID is not None:
        body.update({"challengeID": challengeID})
    # Only send webAuthnKeyID if the argument was provided, dont send null values
    if webAuthnKeyID is not None:
        body.update({"webAuthnKeyID": webAuthnKeyID})
    # Only send attestationObject if the argument was provided, dont send null values
    if attestationObject is not None:
        body.update({"attestationObject": attestationObject})
    # Only send clientData if the argument was provided, dont send null values
    if clientData is not None:
        body.update({"clientData": clientData})
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

@register_command(
    extending=("authentication", "v1", "signature"),
    module=argus_cli_module
)
def get_public_key_enrollment_options(
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
) -> dict:
    """Get enrollment options before enrolling new public key (PUBLIC)
    
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

    route = "/authentication/v1/signature/enroll".format()

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

    query_parameters = {}
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

@register_command(
    extending=("authentication", "v1", "signature"),
    module=argus_cli_module
)
def get_webauthn_authentication_options(
    userName: str = None,
    domain: str = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
) -> dict:
    """Request parameters for authenticating using webauthn (DEPRECATED, use POST /signature/webauthn/authentication/challenge) (PUBLIC)
    
    :param str userName: Username of the user preparing to authenticate
    :param str domain: User domain
    :param json: return the response's body as a ``dict`` parsed from json. ``True`` by
      default. If set to false, the raw ``requests.Response`` object will be returned.
    :param verify: path to a certificate bundle or boolean indicating whether SSL
      verification should be performed.
    :param apiKey: Argus API key.
    :param authentication: authentication override
    :param server_url: API base URL override
    :param body: body of the request. other parameters will override keys defined in the body.
    :raises ValidationErrorException: on 412
    :raises IfTheCurrentIpHasSubmittedTooManyChallengesWithinAShortTimeFrame.TheClientShouldSlowDown.Exception: on 429
    :raises ArgusException: on other status codes
    
    :returns: dictionary translated from JSON
    """

    route = "/authentication/v1/signature/webauthn/authentication".format(userName=userName,
        domain=domain)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

    query_parameters = {}
    # Only send userName if the argument was provided, dont send null values
    if userName is not None:
        query_parameters.update({"userName": userName})
    
    # Only send domain if the argument was provided, dont send null values
    if domain is not None:
        query_parameters.update({"domain": domain})
    
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

@register_command(
    extending=("authentication", "v1", "signature"),
    module=argus_cli_module
)
def get_webauthn_create_options(
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
) -> dict:
    """Request parameters for enrolling new webauthn key (Deprecated, use POST /signature/webauthn/enroll/challenge instead) (PUBLIC)
    
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
    :raises NotFoundException: on 404
    :raises ValidationErrorException: on 412
    :raises ArgusException: on other status codes
    
    :returns: dictionary translated from JSON
    """

    route = "/authentication/v1/signature/webauthn/enroll".format()

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

    query_parameters = {}
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

@register_command(
    extending=("authentication", "v1", "signature"),
    module=argus_cli_module
)
def get_webauthn_user_authorization_options(
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
) -> dict:
    """Request an webauthn validation token to validate user presence. The returned token must be used when requesting authorization token. (INTERNAL)
    
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
    :raises NotFoundException: on 404
    :raises ValidationErrorException: on 412
    :raises ArgusException: on other status codes
    
    :returns: dictionary translated from JSON
    """

    route = "/authentication/v1/signature/webauthn/authorize".format()

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

    query_parameters = {}
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

@register_command(
    extending=("authentication", "v1", "signature"),
    module=argus_cli_module
)
def list_public_keys(
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
    """List current user enrolled public keys (PUBLIC)
    
    :param int limit: Maximum number of values to return
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
    :raises AccessDeniedException: on 403
    :raises NotFoundException: on 404
    :raises ValidationErrorException: on 412
    :raises ArgusException: on other status codes
    
    :returns: dictionary translated from JSON
    """

    route = "/authentication/v1/signature".format(limit=limit,
        offset=offset)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

    query_parameters = {}
    # Only send limit if the argument was provided, dont send null values
    if limit is not None:
        query_parameters.update({"limit": limit})
    
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

@register_command(
    extending=("authentication", "v1", "signature"),
    module=argus_cli_module
)
def request_webauthn_authentication_challenge(
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
    """Request parameters for authenticating using webauthn (PUBLIC)
    
    :param str userName: Username to authenticate
    :param str domain: User domain
    :param str password: Static Argus\-password for user
    :param json: return the response's body as a ``dict`` parsed from json. ``True`` by
      default. If set to false, the raw ``requests.Response`` object will be returned.
    :param verify: path to a certificate bundle or boolean indicating whether SSL
      verification should be performed.
    :param apiKey: Argus API key.
    :param authentication: authentication override
    :param server_url: API base URL override
    :param body: body of the request. other parameters will override keys defined in the body.
    :raises ValidationErrorException: on 412
    :raises IfTheCurrentIpHasSubmittedTooManyChallengesWithinAShortTimeFrame.TheClientShouldSlowDown.Exception: on 429
    :raises ArgusException: on other status codes
    
    :returns: dictionary translated from JSON
    """

    route = "/authentication/v1/signature/webauthn/authentication/challenge".format()

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}
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

@register_command(
    extending=("authentication", "v1", "signature"),
    module=argus_cli_module
)
def request_webauthn_enrollment_challenge(
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
) -> dict:
    """Request parameters for enrolling new webauthn key (PUBLIC)
    
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
    :raises NotFoundException: on 404
    :raises ValidationErrorException: on 412
    :raises ArgusException: on other status codes
    
    :returns: dictionary translated from JSON
    """

    route = "/authentication/v1/signature/webauthn/enroll/challenge".format()

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

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

@register_command(
    extending=("authentication", "v1", "signature"),
    module=argus_cli_module
)
def revoke_key(
    keyID: int,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
) -> dict:
    """Revoke public key (PUBLIC)
    
    :param int keyID: ID of key to revoke
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

    route = "/authentication/v1/signature/{keyID}".format(keyID=keyID)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

    query_parameters = {}
    log.debug("DELETE %s (headers: %s, body: %s)" % (route, str(headers), str(body) or ""))

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

@register_command(
    extending=("authentication", "v1", "signature"),
    module=argus_cli_module
)
def webauthn_authentication(
    requestedAuthorizations: str = None,
    userName: str = None,
    domain: str = None,
    webauthnKeyID: str = None,
    challengeID: str = None,
    authenticatorData: str = None,
    clientData: str = None,
    signature: str = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
) -> dict:
    """Initiate a new user session using WebAuthn authentication (PUBLIC)
    
    :param list requestedAuthorizations: Allow client to request authorizations as part of the authentication transaction. The client is not guaranteed to get the requested authorizations. The setPassword authorization is only returned if the current user has the FORCE\_PW\_CHANGE flag set.
    :param str userName: Username to authenticate
    :param str domain: User domain
    :param str webauthnKeyID: The webauthn key ID of the selected webauthn key
    :param str challengeID: The challenge ID returned from the GET \/webauthn\/authenticate
    :param str authenticatorData: The authenticator data structure from the webauthn invocation
    :param str clientData: The clientDataJSON structure from the webauthn invocation
    :param str signature: The signature structure from the webauthn invocation
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

    route = "/authentication/v1/signature/webauthn/authentication".format()

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
    # Only send webauthnKeyID if the argument was provided, dont send null values
    if webauthnKeyID is not None:
        body.update({"webauthnKeyID": webauthnKeyID})
    # Only send challengeID if the argument was provided, dont send null values
    if challengeID is not None:
        body.update({"challengeID": challengeID})
    # Only send authenticatorData if the argument was provided, dont send null values
    if authenticatorData is not None:
        body.update({"authenticatorData": authenticatorData})
    # Only send clientData if the argument was provided, dont send null values
    if clientData is not None:
        body.update({"clientData": clientData})
    # Only send signature if the argument was provided, dont send null values
    if signature is not None:
        body.update({"signature": signature})

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

@register_command(
    extending=("authentication", "v1", "signature"),
    module=argus_cli_module
)
def webauthn_user_authorization(
    operation: str = None,
    context: dict = None,
    nextURI: str = None,
    webauthnKeyID: str = None,
    challengeID: str = None,
    authenticatorData: str = None,
    clientData: str = None,
    signature: str = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
) -> dict:
    """Request an authorization token using a WebAuthn signature (INTERNAL)
    
    :param str operation: The name of the operation to authorize
    :param dict context: Context variables to scope this authorization. All context variables required by the executing service must be present and equal to those provided here.
    :param str nextURI: The URI to redirect\/route to after successful authorization. The URI will be validated according to policy. The authorization token returned from successful authorization should be appended as a query parameter to this URI.
    :param str webauthnKeyID: The webauthn key ID of the selected webauthn key
    :param str challengeID: The challenge ID returned from the GET \/webauthn\/authenticate
    :param str authenticatorData: The authenticator data structure from the webauthn invocation
    :param str clientData: The clientDataJSON structure from the webauthn invocation
    :param str signature: The signature structure from the webauthn invocation
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
    :raises NotFoundException: on 404
    :raises ValidationErrorException: on 412
    :raises ArgusException: on other status codes
    
    :returns: dictionary translated from JSON
    """

    route = "/authentication/v1/signature/webauthn/authorize".format()

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
    # Only send webauthnKeyID if the argument was provided, dont send null values
    if webauthnKeyID is not None:
        body.update({"webauthnKeyID": webauthnKeyID})
    # Only send challengeID if the argument was provided, dont send null values
    if challengeID is not None:
        body.update({"challengeID": challengeID})
    # Only send authenticatorData if the argument was provided, dont send null values
    if authenticatorData is not None:
        body.update({"authenticatorData": authenticatorData})
    # Only send clientData if the argument was provided, dont send null values
    if clientData is not None:
        body.update({"clientData": clientData})
    # Only send signature if the argument was provided, dont send null values
    if signature is not None:
        body.update({"signature": signature})

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

#: **DEPRECATED** : ``get_webauthn_create_options_1`` is an alias for ``get_webauthn_create_options``. Exists
#: only for backward compatibility - **do not use** - use ``get_webauthn_create_options`` instead.
get_webauthn_create_options_1 = register_command(
    extending=("authentication", "v1", "signature"),
    module=argus_cli_module,
    alias="get_webauthn_create_options_1"
)(deprecated_alias("get_webauthn_create_options_1")(get_webauthn_create_options))
#: **DEPRECATED** : ``list_2`` is an alias for ``list_public_keys``. Exists
#: only for backward compatibility - **do not use** - use ``list_public_keys`` instead.
list_2 = register_command(
    extending=("authentication", "v1", "signature"),
    module=argus_cli_module,
    alias="list_2"
)(deprecated_alias("list_2")(list_public_keys))