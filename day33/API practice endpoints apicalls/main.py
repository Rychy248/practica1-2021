import requests #we need to install it
# requests documentation https://docs.python-requests.org/en/latest/

# ISS WEB  http://open-notify.org/Open-Notify-API/ISS-Location-Now/
# API endpoint  http://api.open-notify.org/iss-now.json

response = requests.get(url="http://api.open-notify.org/iss-now.json")

print(response)
# in this point it's a reponse
# like this, <Response [200]>, and it's code

if response.status_code == 404:
    raise Exception("That resources dosen't exist")
elif response.status_code == 401:
    raise Exception("You're not autorised to acces this data")
elif response.status_code != 200:
    raise Exception("Bad response from ISS API")

#Reverse gecoding tool https://www.latlong.net/Show-Latitude-Longitude.html
data = response.json()
print(data)
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
iss_position = (longitude,latitude)
print(f"ISS position {iss_position}")



#https://httpstatuses.com/
#HTTP REPONSES CODE s
# 1xx Informational | hold on
    # 100 Continue
    # 101 Switching Protocols
    # 102 Processing (WebDAV)
#2xx Succes     | Here you go
    # 200 ok, succed
    # 202 Accepted
    # The 202 response is intentionally non-committal. Its purpose is to allow a server to accept a request for some other process (perhaps a batch-oriented process that is only run once per day) without requiring that the user agent's connection to the server persist until the process is completed. The entity returned with this response SHOULD include an indication of the request's current status and either a pointer to a status monitor or some estimate of when the user can expect the request to be fulfilled.
    # 203 Non-Authoritative Information
    # 204 No Content
    # 205 Reset Content
    # 206 Partial Content
    # 207 Multi-Status (WebDAV)
    # 208 Already Reported (WebDAV)
    # 226 IM Used 
# 3xx Redirection | Go Away
    # 300 Multiple Choices
    # 301 Moved Permanently
    # 302 Found
    # 303 See Other
    # 304 Not Modified
    # 305 Use Proxy
    # 306 (Unused)
    # 307 Temporary Redirect
    # 308 Permanent Redirect (experimental)
# 4xx Client Error | You Screwed Up
    # 400 Bad Request
    # 401 Unauthorized
    # 402 Payment Required
    # 403 Forbidden
    # 404 Not Found
    # 405 Method Not Allowed
    # 406 Not Acceptable
    # 407 Proxy Authentication Required
    # 408 Request Timeout
    # 409 Conflict
    # 410 Gone
    # 411 Length Required
    # 412 Precondition Failed
    # 413 Request Entity Too Large
    # 414 Request-URI Too Long
    # 415 Unsupported Media Type
    # 416 Requested Range Not Satisfiable
    # 417 Expectation Failed
    # 418 I'm a teapot (RFC 2324)
    # 420 Enhance Your Calm (Twitter)
    # 422 Unprocessable Entity (WebDAV)
    # 423 Locked (WebDAV)
    # The 424 (Failed Dependency) status code means that the method could not be performed on the resource because the requested action depended on another action and that action failed. For example, if a command in a PROPPATCH method fails, then, at minimum, the rest of the commands will also fail with 424 (Failed Dependency).
    # 425 Reserved for WebDAV
    # 426 Upgrade Required
    # 428 Precondition Required
    # 429 Too Many Requests
    # 431 Request Header Fields Too Large
    # 444 No Response (Nginx)
    # 449 Retry With (Microsoft)
    # 450 Blocked by Windows Parental Controls (Microsoft)
    # 451 Unavailable For Legal Reasons
# 5xx Server Error | Screwed Up
    # 500 Internal Server Error
    # 501 Not Implemented
    # 502 Bad Gateway
    # 503 Service Unavailable
    # 504 Gateway Timeout
    # 505 HTTP Version Not Supported
    # 506 Variant Also Negotiates (Experimental)
    # 507 Insufficient Storage (WebDAV)
    # 508 Loop Detected (WebDAV)
    # 509 Bandwidth Limit Exceeded (Apache)
    # 510 Not Extended
    # 511 Network Authentication Required
    # 598 Network read timeout error
    # 599 Network connect timeout error