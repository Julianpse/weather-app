import json
import requests

from weather import *
from app import *

#Iterates through citylist.json to check if city input is valid - still need to hook up to main app 
def search_city_dict(city_input):
    with open ("citylist.json") as city_list:
        city_dict = json.load(city_list)

    for i in city_dict:
        if i["name"] == city_input:
            valid_city = True
            return valid_city
