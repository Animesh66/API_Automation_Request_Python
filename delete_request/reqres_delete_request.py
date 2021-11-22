import requests

request_uri = "https://reqres.in/api/users/327"

delete_response = requests.delete(request_uri)
print(delete_response.url)
print(delete_response.text)
print(delete_response.status_code)
