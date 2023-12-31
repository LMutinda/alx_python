"""
Take URL from user input, send request to URL and print value of variable X-Request-Id in the response header
"""
import requests
import sys

url = sys.argv[1]
response = requests.get(url)
d = response.headers
try:
    x = d.get("X-Request-Id")
    print (x)
except:
    x = None
    print(x)