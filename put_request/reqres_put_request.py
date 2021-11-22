import requests
import json

request_uri = "https://reqres.in/api/users"
file = open('put_request.json', 'r')
payload = file.read()
payload_json = json.loads(payload)
put_response = requests.put(request_uri, data=payload_json)
put_response = requests.put(request_uri, json=payload_json)
print(put_response.content)
print(put_response.status_code)