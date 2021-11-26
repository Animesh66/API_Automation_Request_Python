import requests

session = requests.Session()  # creating a session
employee = {"Employee": "Animesh"}
company = {"Company": "EPAM"}
set_cookie_url = "https://httpbin.org/cookies/set"
get_cookie_url = "https://httpbin.org/cookies"
session.get(set_cookie_url, params=employee)  # setting the cookie in the session
session.get(set_cookie_url,params=company)  # setting the cookie in the session
response = session.get(get_cookie_url)
print(response.text)
