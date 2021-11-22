import requests
import json
import jsonpath

request_uri = "https://reqres.in/api/users"
file = open('post_request.json', 'r')
payload = file.read()
payload_json = json.loads(payload)
post_response = requests.post(request_uri, data=payload_json)
print(post_response.content)
print(post_response.status_code)
fetch_id = jsonpath.jsonpath(post_response.json(), "id")
print(fetch_id[0])
