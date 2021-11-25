import requests
import json
from jsonpath import jsonpath

cookie_name = {"session_id": "cookie"}

request_uri = "https://httpbin.org/cookies"
response_cookies = requests.get(request_uri,cookies=cookie_name)
print(response_cookies.text)
print(response_cookies.cookies)
