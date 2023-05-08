from dotenv import load_dotenv
import os
from city import cities 

# List of cities to fetch weather data from
CITY_LIST = cities

# Loads environment variables from .env file
load_dotenv()

# Access environment variables
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
