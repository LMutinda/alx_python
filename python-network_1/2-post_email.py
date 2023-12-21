"""
Take a user URL and an email address, send a POST request to the passed URL with the email as a parameter, and finally display the body of the response.
"""

import requests 
import sys 



url = sys.argv[1]
email = sys.argv[2]

payload = {'email': email}

response = requests.post(url, data=payload)
print(response.text)