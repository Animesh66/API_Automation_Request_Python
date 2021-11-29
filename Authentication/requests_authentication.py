import requests
from requests.auth import HTTPBasicAuth
from requests.auth import HTTPDigestAuth
from requests_oauthlib import OAuth1

#    ******* Basic Authentication *******

basic_auth_url = "https://httpbin.org/basic-auth/user/passwd"
basic_response = requests.get(basic_auth_url, auth=HTTPBasicAuth('user', 'passwd1'))
print("Basic Auth status code: ", basic_response.status_code)

#    ******* Bearer Authentication *******

bearer_Auth_url = "https://httpbin.org/bearer"
bearer_header = {"Authorization": "Bearer {Access-Token}"}
bearer_response = requests.get(bearer_Auth_url, headers=bearer_header)  # Bearer token is passed as a header
print("Bearer Auth status code: ", bearer_response.status_code)
print("Bearer Response: ", bearer_response.text)

#    ******* Digestive Authentication *******


#    ******* OAuth1 Authentication *******
