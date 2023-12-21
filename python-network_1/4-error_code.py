"""
Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response.

If the HTTP status code is greater than or equal to 400, print: Error code: followed by the value of the HTTP status code
You must use the packages requests and sys
You are not allowed to import packages other than requests and sys
You dont need to check arguments passed to the script (number or type)
"""

import requests 
import sys

url = sys.argv[1]
response = requests.get(url)
status = response.status_code
if int(status) >= 400:
    print(" Error code: {}".format(status))

else:
    print("Regular request")