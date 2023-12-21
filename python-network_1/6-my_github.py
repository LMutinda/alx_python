"""
Write a Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id

    -You must use Basic Authentication with a personal access token as password to access to your information (only read:user permission is needed)
    -The first argument will be your username
    -The second argument will be your password (in your case, a personal access token as password)
    -You must use the package requests and sys

"""

import requests 
import sys 

url = "https://api.github.com/user"

username = sys.argv[1]
password = sys.argv [2]

auth = (username,password)

response = requests.get(url, auth = auth )

try:
    # Attempt to decode JSON using response.json()
    json_data = response.json()

    if 'id' in json_data:
        # Display the user ID
        print("Your GitHub user ID is:", json_data['id'])
    else:
        # Display an error message if the response does not contain the user ID
        print('None')
except ValueError:
    # Display an error message if decoding fails
    print("Not a valid JSON. Response:", response.text)