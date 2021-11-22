import requests

request_uri = "https://reqres.in/api/users"
query_params = {'page': '2', 'delay': ['3', '5']}  # This is used for generating the query parameters
request_header = {'Accept': 'application/json'}
get_response = requests.get(request_uri, params=query_params,headers=request_header)
print(get_response.url)
print(get_response.status_code)
print(get_response.content)
print(get_response.headers['Content-Type'])
print(get_response.headers)
print(get_response.cookies)
