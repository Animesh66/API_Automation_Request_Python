import requests
from requests import Session

session = Session()  # creating a session
employee = {"Employee": "Animesh"}
company = {"Company": "EPAM"}
set_cookie_url = "https://httpbin.org/cookies/set"
get_cookie_url = "https://httpbin.org/cookies"
session.get(set_cookie_url, params=employee)  # setting the cookie in the session
session.get(set_cookie_url, params=company)  # setting the cookie in the session
response = session.get(get_cookie_url)
print(response.text)
response.close()  # close existing session

# Creating a new session

session_two = Session()
request_header = {"Content-Type": "multipart/form-data"}
session_two_header = session_two.headers.update(request_header)
response_two = session_two.get("https://httpbin.org", headers=session_two_header)
print(response_two.request.headers)
print(response_two.headers)
