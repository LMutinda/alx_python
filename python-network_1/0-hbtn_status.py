"""
Make a request to a server
Request URL: https://alu-intranet.hbtn.io/status
Request Method: GET
"""
import requests

url = "https://alu-intranet.hbtn.io/status"

response = requests.get(url)
print("Body response:")
print("\t- type: {}".format(type(response.text)))
print("\t- content: {}".format(response.text))