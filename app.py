from flask import Flask, jsonify, abort, request
from dotenv import load_dotenv
from pymongo import MongoClient
import os
import requests

app = Flask(__name__)

load_dotenv()

IS_DEVELOPMENT = os.environ.get('IS_DEVELOPMENT')

OPENWEATHERMAP_API_KEY = os.environ.get('OPENWEATHERMAP_API_KEY')
OPENWEATHERMAP_URL = os.environ.get('OPENWEATHERMAP_URL')

MONGODB_URI = os.environ.get('MONGODB_URI')

client = MongoClient(MONGODB_URI)
db = client['weather_logs']
collection = db['logs']

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
        abort(500, description=f"Failed to get weather data. \n {response.text}")

    data = response.json()

    query = {
        'city': city,
        'lat': lat,
        'lon': lon,
        'response': data
    }
    collection.insert_one(query)

    return jsonify(data)


@app.route('/logs/', methods=['GET'])
def get_logs():
    logs = list(collection.find())

    for query in logs:
        query['_id'] = str(query['_id'])

    return jsonify(logs)

if __name__ == '__main__':
    app.run(debug=IS_DEVELOPMENT)
