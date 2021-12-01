import requests
from requests.auth import HTTPBasicAuth
from requests.auth import HTTPDigestAuth
from requests_oauthlib import OAuth1

#                ******* Basic authentication *******

basic_auth_url = "https://httpbin.org/basic-auth/user/passwd"
basic_response = requests.get(basic_auth_url, auth=HTTPBasicAuth('user', 'passwd1'))
print("Basic Auth status code: ", basic_response.status_code)

#               ******* Bearer authentication *******

bearer_Auth_url = "https://httpbin.org/bearer"
bearer_header = {"Authorization": "Bearer {Access-Token}"}
bearer_response = requests.get(bearer_Auth_url, headers=bearer_header)  # Bearer token is passed as a header
print("Bearer Auth status code: ", bearer_response.status_code)
print("Bearer Response: ", bearer_response.text)

#               ******* Digestive authentication *******

digest_Auth_url = "https://httpbin.org/digest-auth/auth/user/passwd"
digest_response = requests.get(digest_Auth_url, auth=HTTPDigestAuth('user', 'passwd'))  # Bearer token is passed as a
# header
print("Digest Auth status code: ", digest_response.status_code)
print("Digest Response: ", digest_response.text)

#               ******* OAuth1 authentication *******

oauth_url = "https://authorization-server.com/token"
oauth = OAuth1('grant_type=authorization_code', 'client_id=hajshdah1212')
oauth_response = requests.get(oauth_url,auth=oauth)
print("OAuth1 status code: ", oauth_response.status_code)
