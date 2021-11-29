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
print(response_ggl.cookies)
for item in items:
    print(item)

# Send multiple cookies through RequestCookieJar()

cookie_jar = RequestsCookieJar()  # contains multiple cookies
cookie_jar.set("Employee Name", "Animesh", domain="httpbin.org", path="/cookies")  # add cookie to RequestCookieJar
cookie_jar.set("Company", "EPAM", domain="httpbin.org", path="/cookies2")
response_new = requests.get(request_uri, cookies=cookie_jar)  # providing multiple cookies in RequestCookieJar
print(response_new.text)
