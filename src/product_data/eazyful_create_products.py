import os
import requests
from csv import reader

CURRENT_WORKING_DIRECTORY = os.getcwd()
PRODUCT_FILE = "{}\\product_data\\product_data_04232021.csv".format(CURRENT_WORKING_DIRECTORY)
PRODUCT_ENDPOINT = "http://127.0.0.1:8000/foods/products/"

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjIyNzIwNjQ0LCJqdGkiOiIwZDA1NDU1NmFmNDg0MWYwOTVkMWFiMjNiNzZkMmFmNyIsInVzZXJfaWQiOiI2ZDg1ZWZhZS1lYTQzLTQxYzktYTAyOC1mZTVlMTkyYTIyYjQifQ.-eQmBwA3uoSxS60QFpRnmOOGsENhfHefnjYXezxaDH-XaBO_Iz94HjH1OUKfODYUD1mHxO9hDf8SFatrFD7RRA"

headers = {"Authorization": "Bearer {}".format(token)}

with open(PRODUCT_FILE, "r") as obj:
    csv_file = reader(obj)
    for row in csv_file:
        data = {
            "name": row[0],
            "serving_size": row[1],
            "calories": row[2],
            "protein": row[3],
            "carbohydrate": row[4],
            "total_fat": row[5],
            "sugars": row[6],
            "saturated_fats": row[7],
            "polyunsaturated_fats": row[8],
            "monosaturated_fats": row[9],
            "trans_fats": row[10],
            "cholesterol": row[11],
            "sodium": row[12],
            "biotin": row[13],
            "choline": row[14],
            "folic": row[15],
            "niacin": row[16],
            "pantohenic": row[17],
            "thiamin": row[18],
            "vitamin_a": row[19],
            "vitamin_b_six": row[20],
            "vitmain_b_twelve": row[21],
            "vitamin_c": row[22],
            "vitamin_d": row[23],
            "vitamin_e": row[24],
            "vitamin_k": row[25],
            "calcium": row[26],
            "chlorine": row[27],
            "chromium": row[28],
            "copper": row[29],
            "iodine": row[30],
            "iron": row[31],
            "magnesium": row[32],
            "manganese": row[33],
            "molybdenum": row[34],
            "phosphorous": row[35],
            "potassium": row[36],
            "selenium": row[37],
            "zinc": row[38],
            "ingredients": row[39],
            "allergens_and_warnings": row[40],
            "brand_id": row[41]
        }
        requests.post(PRODUCT_ENDPOINT, data=data, headers=headers)
        print("Finished creating {}".format(row[0]))