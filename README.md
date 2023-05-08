# Weather Analysis Dashboard

## Overview

The Weather Analysis Dashboard project is an interactive data visualization tool designed to display and analyze real-time weather data for cities across the globe, with a focus on Pernambuco, Brazil. This project aims to provide valuable insights into weather patterns, trends, and comparisons, making it an essential resource for researchers, meteorologists, and anyone interested in understanding regional climates.

![Dashboard Screenshot]![image](https://user-images.githubusercontent.com/91219935/236701627-7d406c65-e003-4223-aab5-5e7daf76a6f8.png)

## Features

- Updated daily weather data from OpenWeatherMap API
- Data storage and management with PostgreSQL database
- Interactive visualizations powered by Power BI
- Comprehensive analysis of temperature, humidity, and pressure patterns
- User-friendly interface for exploring and comparing weather data across cities

## Future features

- Set up a cron to play updated data every day at 6 AM
- Improve the look and design of the dashboard

## Technical Stack

- Data Ingestion: Python, OpenWeatherMap API
- Data Transformation: Python, NumPy, pandas
- Data Storage: PostgreSQL
- Data Visualization: Power BI
- Version Control: Git, GitHub

## Getting Started

To get started with the Weather Analysis Dashboard project, please follow these steps:

1. Clone this repository to your local machine.
2. Obtain an API key from OpenWeatherMap and add it to the `config.py` file.
3. Set up a PostgreSQL database and update the connection string in the `load_data.py` file.
4. Run the `main.py` script to fetch, process, and store weather data.
5. Open the Power BI file, connect it to your PostgreSQL database, and explore the visualizations.

## Contributing

We welcome contributions to improve the Weather Analysis Dashboard project. If you would like to contribute, please follow these steps:

1. Fork this repository.
2. Create a new branch with a descriptive name.
3. Make your changes and commit them to your branch.
4. Create a pull request and provide a detailed description of your changes.

We will review your changes and provide feedback as soon as possible.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any inquiries or suggestions, please feel free to contact the project maintainers.
