import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from config import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT

# Connect to PostgreSQL server
connection = psycopg2.connect(user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cursor = connection.cursor()

# Create a new database
db_name = "weather_db"
cursor.execute(f"CREATE DATABASE {db_name};")
cursor.close()
connection.close()

# Connect to the new database
connection = psycopg2.connect(user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT, database=db_name)
cursor = connection.cursor()


# Create the weather_data table if it doesn't already exist
cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather_data (
            id SERIAL PRIMARY KEY,
            city VARCHAR(255) NOT NULL,
            country CHAR(2) NOT NULL,
            temperature FLOAT NOT NULL,
            humidity INT NOT NULL,
            pressure INT NOT NULL
        );
    """)

# Commit the changes and close the connection
connection.commit()
cursor.close()
connection.close()




# Function that will store the data in the database
def load_weather_data(df):
    # Convert the DataFrame to a list of tuples
    weather_data_tuples = [tuple(x) for x in df.to_records(index=False)]

    # Connect to the database
    connection_string = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/weather_db"
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()

    # Insert the weather data into the weather_data table
    insert_query = """
        INSERT INTO weather_data (city, country, temperature, humidity, pressure)
        VALUES (%s, %s, %s, %s, %s)
    """

    # Convert numpy.int64 values to int before inserting into the database
    converted_weather_data_tuples = [
        (city, country, float(temperature), int(humidity), int(pressure))
        for city, country, temperature, humidity, pressure in weather_data_tuples
    ]

    cursor.executemany(insert_query, converted_weather_data_tuples)

    # Commit the changes and close the connection
    conn.commit()
    cursor.close()
    conn.close()
