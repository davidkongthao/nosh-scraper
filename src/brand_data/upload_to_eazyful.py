import os
import requests
from csv import reader
import threading

CURRENT_WORKING_DIRECTORY = os.getcwd()
BRAND_FILE = "{}\\brand_data\\brand.csv".format(CURRENT_WORKING_DIRECTORY)
BRAND_ENDPOINT = "http://127.0.0.1:8000/foods/brands/"

token = ""
headers = {"Authorization": "Bearer {}".format(token)}

with open(BRAND_FILE, "r") as obj:
    csv_file = reader(obj)
    for row in csv_file:
        data = {
            "name": row[0],
            "website": row[1],
            "description": row[2]
        }

        if row[3] == "" or row[3] == None:
            requests.post(BRAND_ENDPOINT, data=data, headers=headers)
        else:
            logo_path = row[3]
            logo = {"logo": open(logo_path, "rb")}
            requests.post(BRAND_ENDPOINT, files=logo, data=data, headers=headers)

        print("Added {} to database.".format(row[0]))


