import requests


# Send Cookies to Server

cookie_name = {"session_id": "cookie_12098712"}
request_uri = "https://httpbin.org/cookies"
response_cookies = requests.get(request_uri,cookies=cookie_name)
print(response_cookies.text)
print(response_cookies.cookies)

# Receive Cookies from Server
