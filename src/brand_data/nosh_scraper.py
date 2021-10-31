import os
import time
import shutil
import requests
import uuid
from csv import writer, DictWriter
from bs4 import BeautifulSoup
from collections import OrderedDict

"""

This script is meant to scrape www.nosh.com for brands. 

"""

CURRENT_WORKING_DIRECTORY = os.getcwd()
DESTINATION_PATH = "{}\\logos".format(CURRENT_WORKING_DIRECTORY)
BRAND_FILE = "{}\\brand_second.csv".format(CURRENT_WORKING_DIRECTORY)

nosh_main_url = "https://www.nosh.com/brands"

nosh_main_req = requests.get(nosh_main_url)
nosh_brand_soup = BeautifulSoup(nosh_main_req.text, "html.parser")

brand_urls = nosh_brand_soup.find_all("a")

urls = [a["href"] for a in brand_urls]
sub_string = "/brands"
sorted_urls = [url for url in urls if sub_string in url]; sorted_urls.pop(0)
sorted_urls = list(OrderedDict.fromkeys(sorted_urls))[1400:]

for url in sorted_urls:
    try:
        brand_url = "https://www.nosh.com{}".format(url)
        req = requests.get(brand_url)
        brand_page = BeautifulSoup(req.text, "html.parser")
        
        print("Getting information for {}".format(brand_url))

        brand_info = brand_page.find_all("div", {"class": "brand-contact-row"})
        brand_name = brand_page.find("h1", {"class": "main-title"}).get_text()

        try:
            brand_url = brand_page.find_all("div", {"class": "brand-contact-row"})[1].find_all("a")[0].get_text()
        except (AttributeError, IndexError):
            brand_url = None

        try:
            brand_description = brand_page.find_all("div", {"class": "brand-overview-info"})[0].find("p").get_text()
        except (AttributeError, IndexError):
            brand_description = "No information provided."

        images = brand_page.find_all("img")
        image_urls = [img["src"] for img in images]
        sub_string = "/logos"
        try:
            logo_url = "https://{}".format([url for url in image_urls if sub_string in url][0].split("//")[1])
            filename = logo_url.split("/")[-1]
            filename_split = filename.split(".")
            new_filename = "{}_{}.{}".format(filename_split[1], uuid.uuid4(), filename_split[-1])
            logo_req = requests.get(logo_url, stream=True)
            logo_req.raw.decode_content = True
            
            with open(filename, "wb") as f:
                shutil.copyfileobj(logo_req.raw, f)
            
            os.rename(filename, new_filename)
            shutil.move("{}\\{}".format(CURRENT_WORKING_DIRECTORY, new_filename), DESTINATION_PATH)
            LOGO_FILE_PATH = "{}\\{}".format(DESTINATION_PATH, new_filename)
            
        except (AttributeError, IndexError, ConnectionError, ConnectionAbortedError, ConnectionRefusedError, ConnectionAbortedError):
            LOGO_FILE_PATH = None

        field_names = ["Name", "Website", "Description", "Logo"]
        data = {"Name": brand_name, "Website": brand_url, "Description": brand_description, "Logo": LOGO_FILE_PATH}

        with open(BRAND_FILE, "a", newline="") as outfile:
            writer_obj = DictWriter(outfile, fieldnames=field_names)
            writer_obj.writerow(data)
            outfile.close()
    except (ConnectionError):
        pass



