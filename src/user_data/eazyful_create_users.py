import os
import requests
import threading
from csv import reader

CURRENT_WORKING_DIRECTORY = os.getcwd()
USERS_FILE = "{}\\user_data\\users_data_new.csv".format(CURRENT_WORKING_DIRECTORY)
USERS_ENDPOINT = "http://127.0.0.1:8000/accounts/users/"

#token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE4MjUxNjM2LCJqdGkiOiI2M2MzZjg2NmUzMGE0YjM4ODQ1NDRhYjU1MjJhZDFkNCIsInVzZXJfaWQiOiI0Y2Q5MTc0Zi0yNjg0LTRkNTYtYWMzYS1mMzNkMjAwMDkzM2UifQ.YlZ6ZMGi8hSxUIf15t9quK3uW9ySyzQQr42_y9DrUtY1iBoJIvtIuBlkq6gObcP0Us21A4EGUqjOzXGjBNJIjg"

#headers = {"Authorization": "Bearer {}".format(token)}

with open(USERS_FILE, "r") as obj:
    csv_file = reader(obj)
    for row in csv_file:
        data = {
            "first_name": row[0],
            "last_name": row[1],
            "email": row[2],
            "username": row[3],
            "password": row[4],
            "password_confirm": row[4]
        }

        requests.post(USERS_ENDPOINT, data=data)
        print("Finished creating user {}.".format(row[3]))