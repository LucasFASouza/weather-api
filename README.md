# Weather API

This is a simple Flask application that provides weather data by interfacing with the OpenWeatherMap API.

## Features

- Get weather data by city name
- Get weather data by latitude and longitude

## Setup

1. Clone the repository
2. Navigate to the project directory
3. Install the required Python packages:
```
pip install -r requirements.txt
```
4. Set the necessary environment variables:
```
OPENWEATHERMAP_API_KEY={your openweather api key}
OPENWEATHERMAP_URL=http://api.openweathermap.org/data/2.5/weather
```
For the daily forecast of the next 5 days, it is necessary to add `/daily` to the URL and provide an appropriate API key. Otherwise, the API will return the forecast in 3-hour intervals for the next 15 hours.

## Usage

Start the Flask application:
```
python app.py
```

The application will start running at http://127.0.0.1:5000.

To get weather data, make a GET request to the /weather endpoint with either a city parameter or lat and lon parameters.

Example:

- By city name: http://127.0.0.1:5000/weather?city=London
- By latitude and longitude: http://127.0.0.1:5000/weather?lat=51.51&lon=-0.13

## Error Handling

The API will return the following error responses:

- 400 Bad Request if neither city nor lat and lon parameters are provided.
- 500 Internal Server Error if there was an error retrieving the weather data.

## License

This project is licensed under the terms of the MIT license.