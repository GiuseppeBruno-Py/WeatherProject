# import the functions we need from the other files
from fetch_data import fetch_weather_data
from transform_data import transform_weather_data
from load_data import load_weather_data

# Function that will orchestrate the execution of our pipeline
def main():
    raw_data = fetch_weather_data()
    transformed_data = transform_weather_data(raw_data)
    load_weather_data(transformed_data)

if __name__ == "__main__":
    main()
