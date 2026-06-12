import os
from flask import Flask, render_template, request, jsonify
import requests
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

app = Flask(__name__)

# OpenWeatherMap API configuration
API_KEY = os.getenv('OPENWEATHER_API_KEY')
BASE_URL = 'https://api.openweathermap.org/data/2.5'

# Default city
DEFAULT_CITY = 'London'


def get_weather_data(city):
    """Fetch current weather data from OpenWeatherMap API"""
    try:
        url = f'{BASE_URL}/weather?q={city}&appid={API_KEY}&units=metric'
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None


def get_forecast_data(city):
    """Fetch 5-day forecast data from OpenWeatherMap API"""
    try:
        url = f'{BASE_URL}/forecast?q={city}&appid={API_KEY}&units=metric'
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching forecast data: {e}")
        return None


def process_forecast(forecast_data):
    """Process forecast data to get daily summaries"""
    if not forecast_data:
        return []
    
    daily_forecasts = {}
    
    for item in forecast_data['list']:
        date = datetime.fromtimestamp(item['dt']).strftime('%Y-%m-%d')
        
        if date not in daily_forecasts:
            daily_forecasts[date] = {
                'date': date,
                'temp_max': item['main']['temp_max'],
                'temp_min': item['main']['temp_min'],
                'description': item['weather'][0]['description'],
                'icon': item['weather'][0]['icon'],
                'humidity': item['main']['humidity'],
                'wind_speed': item['wind']['speed']
            }
        else:
            daily_forecasts[date]['temp_max'] = max(daily_forecasts[date]['temp_max'], item['main']['temp_max'])
            daily_forecasts[date]['temp_min'] = min(daily_forecasts[date]['temp_min'], item['main']['temp_min'])
    
    return list(daily_forecasts.values())[:5]


@app.route('/')
def index():
    """Render the main dashboard page"""
    weather = get_weather_data(DEFAULT_CITY)
    forecast = get_forecast_data(DEFAULT_CITY)
    forecast_data = process_forecast(forecast)
    
    return render_template('index.html', weather=weather, forecast=forecast_data, city=DEFAULT_CITY)


@app.route('/api/weather', methods=['POST'])
def api_weather():
    """API endpoint to fetch weather for a specific city"""
    data = request.get_json()
    city = data.get('city', DEFAULT_CITY)
    
    if not city:
        return jsonify({'error': 'City name is required'}), 400
    
    weather = get_weather_data(city)
    
    if not weather or weather.get('cod') != 200:
        return jsonify({'error': 'City not found'}), 404
    
    forecast = get_forecast_data(city)
    forecast_data = process_forecast(forecast)
    
    return jsonify({
        'weather': weather,
        'forecast': forecast_data
    })


@app.route('/api/cities', methods=['GET'])
def api_cities():
    """API endpoint to get a list of preset cities"""
    cities = ['London', 'New York', 'Tokyo', 'Paris', 'Sydney', 'Dubai', 'Singapore', 'Toronto']
    return jsonify({'cities': cities})


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(error):
    """Handle 500 errors"""
    return render_template('500.html'), 500


if __name__ == '__main__':
    if not API_KEY:
        print('Warning: OPENWEATHER_API_KEY environment variable not set')
    
    app.run(debug=True, host='0.0.0.0', port=5000)
