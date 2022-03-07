#login to digikala.com with user and password then find your account info 
from urllib import request
import requests

s = requests.session()

user, password = input(
    "inter your username and password (user,pass):").split(",")

url = "https://api.digikala.com/v1/user/authenticate/"
data = {"backUrl": "/", "username": user}


print(s.post(url, json=data).text)

url = "https://api.digikala.com/v1/user/login/password/"
data = {"backUrl": "/", "username": user, "password": password}

print(s.post(url, json=data).text)

url = "https://api.digikala.com/v1/profile/personal-info/"

print(s.get(url).text)
