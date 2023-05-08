import requests
from config import OPENWEATHER_API_KEY, CITY_LIST 

# Fetches weather data from the OpenWeather API
def fetch_weather_data():
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    weather_data = []

    for city in CITY_LIST:
        params = {
            "q": city,
            "appid": OPENWEATHER_API_KEY,
            "units": "metric"
        }
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            weather_data.append(response.json())

    return weather_data
