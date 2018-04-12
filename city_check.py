import json
import requests

from weather import *
from app import *

#Iterates through citylist.json to check if city is a valid API query 
def search_city_dict(city_input):
    valid_city = []
    with open ("citylist.json") as city_list:
        city_dict = json.load(city_list)

    for i in city_dict:
        if i["name"] == city_input:
            valid_city.append(city_input)

    return valid_city
