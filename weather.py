import requests
import json
import pprint

#city input is hard coded and receiving a successful API request - Can pass city input from the form after importing the module

city_input = "Houston"

payload = {'q': city_input, "APPID": "ec4678cf0af0d362007a3348b7c53b7a", "units": "imperial"}
r = requests.get('https://api.openweathermap.org/data/2.5/weather', params = payload)


# Stores data in data.json
data = r.json()
with open('data.json', 'w') as fh:
  json.dump(data, fh)
