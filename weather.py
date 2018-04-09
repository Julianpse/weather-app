import requests
import json

from app import * 

def weather_request(city_input):
    payload = {'q': city_input, "APPID": "ec4678cf0af0d362007a3348b7c53b7a", "units": "imperial"}
    r = requests.get('https://api.openweathermap.org/data/2.5/weather', params = payload)

    data = r.json()

    # Stores data in data.json
    with open('data.json', 'w') as fh:
        json.dump(data, fh)

#Opens Data to be rendered on results page
with open("data.json") as json_file:
    json_data = json.load(json_file)
