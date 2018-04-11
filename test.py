import json
import datetime
import psycopg2
import requests

#Opens Data to be rendered on results page
with open("test.json") as json_file:
    json_data = json.load(json_file)

#prints temperature
print(int(json_data["main"]["temp"]))

#prints what the sky is
print(json_data["weather"][0]["main"])

#prints the location
print(json_data["name"])

#prints the icon number
print(json_data["weather"][0]["icon"])

#prints the icon description
print(json_data["weather"][0]["description"])


#prints the timestamp and converts it into readable
unix_time = json_data["dt"]
readable_time = datetime.datetime.fromtimestamp(int(unix_time)).strftime('%Y-%m-%d %H:%M:%S')
print (readable_time)
