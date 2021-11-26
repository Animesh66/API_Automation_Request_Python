import requests
from requests.cookies import RequestsCookieJar

# Send Cookies to Server

cookie_name = {"session_id": "cookie_12098712"}
request_uri = "https://httpbin.org/cookies"
response_cookies = requests.get(request_uri, cookies=cookie_name)
print(response_cookies.text)
print(response_cookies.cookies)

# Receive Cookies from Server

response_ggl = requests.get("https://google.com")
items = response_ggl.cookies.items()  # This will return a list of tuples
for item in items:
    print(item)
response_jar = RequestsCookieJar()  # contains multiple cookies
response_jar.set("employee", "Animesh", domain="httpbin.org", path="/cookies")
response_new = requests.get(request_uri, cookies=response_jar)  # providing multiple cookies
print(response_new.text)
