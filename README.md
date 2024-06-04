# Weather API

This is a simple Flask application that provides a weather forecast for a given city or coordinates using the OpenWeatherMap API. It also logs each use of the `/weather` endpoint in a MongoDB database and provides an endpoint to retrieve these logs.

## Endpoints

- `/weather/`: Returns a weather forecast for a given city or coordinates. Accepts the following query parameters:
  - `city`: The name of the city to get the weather forecast for.
  - `lat` and `lon`: The latitude and longitude to get the weather forecast for. Both must be provided.

- `/logs/`: Returns a list of all logs, where each log is a use of the `/weather` endpoint.

## Setup

1. Clone this repository.
2. Install the required Python packages: `pip install -r requirements.txt`
3. Set the following environment variables:
   - `OPENWEATHERMAP_API_KEY`: Your OpenWeatherMap API key.
   - `OPENWEATHERMAP_URL`: The URL of the OpenWeatherMap API.
   - `MONGODB_URI`: The URI of your MongoDB database.
4. Run the application: `python app.py`

Typically, the OpenWeatherMap API URL is https://api.openweathermap.org/data/2.5/forecast, which provides weather forecasts in 3-hour intervals for the upcoming 15 hours. However, if you need to access the daily forecast for the next 5 days, you should use the URL https://api.openweathermap.org/data/2.5/forecast/daily. In that case, please ensure that your API key has the appropriate permissions to access this endpoint.

## Docker

If you're using Docker, you can run a MongoDB container with the following command:

```bash
docker pull mongo

docker run --name some-mongo -p 27017:27017 -d mongo
```

Then, set `MONGODB_URI` to `mongodb://localhost:27017/` or the appropriate MongoDB connection string.

## Usage

To get the weather forecast for a city:
```bash
curl "http://localhost:5000/weather/?city=Sao%20Paulo"
```

To get the weather forecast for a set of coordinates:
```bash
curl "http://localhost:5000/weather/?lat=-23.5475&lon=-46.6361"
```

To get the logs:
```bash
curl "http://localhost:5000/logs/"
```