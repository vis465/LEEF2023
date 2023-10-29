import requests

url = "https://www.townscript.com/api/user/loginwithtownscript"

payload = {
    "emailId": "visv6812@gmail.com",
    "password": "sonatec#$1"
}
headers = {
    "accept": "application/json",
    "content-type": "application/x-www-form-urlencoded"
}

response = requests.post(url, data=payload, headers=headers)

print(response.text)