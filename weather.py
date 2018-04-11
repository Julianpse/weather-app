import os

import requests
import json
import psycopg2

from app import *


## This opens the connection to the postgres database
def connect_to_postgres():
    try:
        conn = psycopg2.connect("dbname='weatherapp' user='julianse' host='localhost' password=''")
        cur = conn.cursor()
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

    cur.execute("INSERT INTO weather(city_name, temperature, time_of_day) VALUES (%s, %s, LOCALTIMESTAMP)", (location, temperature))
    cur.execute("SELECT temperature FROM weather WHERE time_of_day > NOW() - INTERVAL '15 minutes' AND city_name ~* %(city)s", {"city": city_input})

    temp = cur.fetchone()
    return temp

    conn.commit()
    cur.close()
    conn.close()
