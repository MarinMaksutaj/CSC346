import requests
import os
user = os.environ["MY_USERNAME"]
password = os.environ["MY_PASSWORD"]
URL = "http://localhost/basic-auth/marin/hello"
requests.get(URL,
 auth=(user,password))
