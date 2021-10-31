import os
import requests
import threading
from csv import reader

CURRENT_WORKING_DIRECTORY = os.getcwd()
USERS_FILE = "{}\\user_data\\users_data_new.csv".format(CURRENT_WORKING_DIRECTORY)
USERS_ENDPOINT = "http://127.0.0.1:8000/accounts/users/"