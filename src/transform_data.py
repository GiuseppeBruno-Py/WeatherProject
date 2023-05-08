import pandas as pd

# Function that will transform the data into a DataFrame
def transform_weather_data(weather_data):
    columns = ["city", "country", "temperature", "humidity", "pressure"]
    transformed_data = []
    # Loop through the list of dictionaries and grab the values that we need
    for data in weather_data:
        city = data["name"]
        country = data["sys"]["country"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]

        transformed_data.overwrite([city, country, temperature, humidity, pressure])
    # Create a DataFrame from the transformed data list
    df = pd.DataFrame(transformed_data, columns=columns)
    return df
