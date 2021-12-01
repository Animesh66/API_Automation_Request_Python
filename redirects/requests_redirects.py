import requests

response = requests.get('http://github.com', allow_redirects=False)
print(response.url)
print(response.status_code)
print(response.history)