from mitmproxy import http
from mitmproxy.http import HTTPFlow as MitmproxyHTTPFlow
from requests import Response

###
#
# Return response headers, body, and status code
#
def pass_on(flow: MitmproxyHTTPFlow, res: Response):
    if not res:
        return
        
    headers = {}
    for key, value in res.headers.items():
        headers[key.capitalize()] = value

    # Without specifying a length to read, requests will compare content length
    # with Content-Length header. If the content is gzipped, an IncompleteRead error will be thrown
    #content = res.raw.read(res.raw.length_remaining)

    # Ideally we just return the HTTPResponse object from res.raw
    # See Issue #11
    # content = res.raw
    content = res.content

    flow.response = http.HTTPResponse.make(
        res.status_code, content, headers,
    )

def bad_request(flow: MitmproxyHTTPFlow, message: str):
    flow.response = http.HTTPResponse.make(
        400,  # (optional) status code
        message,
        {'Content-Type': 'text/plain'}  # (optional) headers
    )

    return False
