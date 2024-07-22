import requests
from datetime import datetime
from config import DB_CONFIG
import mysql.connector
from mysql.connector import Error

API_KEY = 'your_api_key'
LOCATION = 'London'


def fetch_weather_data():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={LOCATION}&appid={API_KEY}&units=metric"
    response = requests.get(url).json()
    temperature = response['main']['temp']
    humidity = response['main']['humidity']
    wind_speed = response['wind']['speed']
    timestamp = datetime.now()

    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO weather (timestamp, temperature, humidity, wind_speed) VALUES (%s, %s, %s, %s)",
            (timestamp, temperature, humidity, wind_speed)
        )
        conn.commit()
    except Error as e:
        print(f"Error: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
