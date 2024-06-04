from flask import Flask, jsonify, abort, request
import os
import requests

app = Flask(__name__)

OPENWEATHERMAP_API_KEY = os.environ.get('OPENWEATHERMAP_API_KEY')
OPENWEATHERMAP_URL = os.environ.get('OPENWEATHERMAP_URL')


@app.route('/weather/', methods=['GET'])
def get_weather():
    city = request.args.get('city')

    lat = request.args.get('lat')
    lon = request.args.get('lon')

    if not city and not (lat and lon):
        abort(400, description="Missing city or lat/lon parameters.")

    params = {
        'appid': OPENWEATHERMAP_API_KEY,
        'lat': lat,
        'lon': lon,
        'q': city,
        'units': 'metric',
        'cnt': 5
    }

    try:
        response = requests.get(OPENWEATHERMAP_URL, params=params)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        abort(500, description="Failed to get weather data.")

    data = response.json()

    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
