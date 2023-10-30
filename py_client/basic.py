import requests

# API - Application programing interface 
# kind of a url. there will be several endpoints in the client
# endpoint = "https://httpbin.org/status/200"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/" # "http://127.0.0.1:8000/"

#use the api that is in this library
# API -> Method (function built into it)   

get_response = requests.get(endpoint, json={"Hello, brother!": 47}) # HTTP Request

# print(get_response.headers)
# print(get_response.text)  #print raw text response
# print(get_response.status_code)

#HTTP Request -> HTML
# REST API HTTP Request -> JSON
# JavaScript Object Notation ` Python Dict`

print(get_response.json())

# print(get_response.status_code) # -> 200