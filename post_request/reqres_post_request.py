import requests
import json
from jsonpath import jsonpath


request_uri = "https://reqres.in/api/users"
file = open('post_request.json', 'r')
payload = file.read()
payload_json = json.loads(payload)  # Converts the file content to a list of dictionary
print(payload_json)
post_response = requests.post(request_uri, data=payload_json)
print(post_response.text)
print(post_response.status_code)
fetch_id = jsonpath(post_response.json(), "id")  # Reads the "id" key from the response JSON and
# returns a list of values of the given key here for the "id" key
print(fetch_id[0])  # Display the first value of the "id" key
