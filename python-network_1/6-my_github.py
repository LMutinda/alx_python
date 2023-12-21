"""
Write a Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id

    -You must use Basic Authentication with a personal access token as password to access to your information (only read:user permission is needed)
    -The first argument will be your username
    -The second argument will be your password (in your case, a personal access token as password)
    -You must use the package requests and sys

"""

import requests 
import sys 

url = "https://docs.github.com/en/rest/users?apiVersion=2022-11-28"

username = sys.argv[1]
password = sys.argv [2]

user = {username: password}

response = requests.post(url, data = user )
data = response.json()
print(data["id"])