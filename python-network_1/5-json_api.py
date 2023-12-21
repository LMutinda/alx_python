"""
Write a Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.

    The letter must be sent in the variable q
    If no argument is given, set q=""
    If the response body is properly JSON formatted and not empty, display the id and name like this: [<id>] <name>
    Otherwise:
        Display Not a valid JSON if the JSON is invalid
        Display No result if the JSON is empty

"""

import requests 
import sys


url = "http://0.0.0.0:5000/search_user"

if len(sys.argv)>=2:
    letter = sys.argv[1]
    
else:
    letter = ''

payload = {'q': letter}


response = requests.post(url, data = payload)

try:
    # Attempt to decode JSON using response.json()
    json_data = response.json()

    if json_data:
        # Display id and name if JSON is not empty
        print("[{}] {}".format(json_data['id'], json_data['name']))
    else:
        # Display 'No result' if JSON is empty
        print("No result")
except ValueError:
        # Display 'Not a valid JSON' if decoding fails
        print("Not a valid JSON")

