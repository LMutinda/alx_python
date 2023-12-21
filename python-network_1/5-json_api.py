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

def is_json(response):
    """
    Method for finding of the response is properly formatted json
    """
    try:
        # Attempt to decode JSON using response.json()
        _ = response.json()
        return True
    except ValueError:
        # If decoding fails, it's not a valid JSON
        return False
    
def is_response_body_empty(response):
    """Check if the content length is 0"""
    return len(response.content) == 0

url = "http://0.0.0.0:5000/search_user"

if len(sys.argv)>=2:
    letter = sys.argv[1]
    
else:
    letter = {'q': ''}

payload = {'q': letter}

response = requests.get(url, data = payload)

if is_json(response):
    if not is_response_body_empty(response):
        print(response)
    else:
        print("No result")

else:
    print("Not a valid JSON")

