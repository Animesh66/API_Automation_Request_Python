import requests
import json

request_uri = "https://reqres.in/api/users"
file = open('patch_request.json', 'r')
payload = file.read()
payload_json = json.loads(payload)
patch_response = requests.put(request_uri, data=payload_json)
patch_response = requests.put(request_uri, json=payload_json)
print(patch_response.content)
print(patch_response.status_code)