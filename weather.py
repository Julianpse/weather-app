import os

import requests
import json
import psycopg2

from app import *
from icons import *
## This opens the connection to the postgres database
def connect_to_postgres():
    try:
        conn
        cur
    except:
        print("I am unable to connect to the database, please check your connection")
    return conn, cur


## This function takes the user's city input, retreives the data from the API and then writes to the database
def weather_request(city_input):
    payload = {'q': city_input, "APPID": "ec4678cf0af0d362007a3348b7c53b7a", "units": "imperial"}
    r = requests.get('https://api.openweathermap.org/data/2.5/weather', params = payload)

    data = r.json()

    location = data["name"]
    temperature = int(data["main"]["temp"])
    weather_id = int(data['weather'][0]["id"])

    cur.execute("INSERT INTO weather(city_name, temperature, time_of_day, weather_id) VALUES (%s, %s, LOCALTIMESTAMP, %s)", (location, temperature, weather_id))
    cur.execute("SELECT temperature, weather_id FROM weather WHERE time_of_day > NOW() - INTERVAL '15 minutes' AND city_name ~* %(city)s", {"city": city_input})

    temp = cur.fetchone()
    id = cur.fetchone()
    return int(temp[0]), int(weather_id)

    conn.commit()
    cur.close()
    conn.close()
