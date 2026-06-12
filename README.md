# Weather Dashboard

A beautiful, responsive weather dashboard built with Python Flask and OpenWeatherMap API.

## Features

- 🌤️ **Current Weather**: Real-time weather information including temperature, humidity, wind speed, and more
- 📅 **5-Day Forecast**: Extended weather forecast for the next 5 days
- 🔍 **City Search**: Search weather for any city in the world
- 📱 **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- 🎨 **Beautiful UI**: Modern, clean interface with smooth animations
- ⚡ **Fast & Reliable**: Powered by OpenWeatherMap's free API tier

## Screenshots

(Add screenshots here after deployment)

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package manager)
- Git

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/AdiosGlitchos/weather-dashboard.git
   cd weather-dashboard
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   
   **On Windows:**
   ```bash
   venv\Scripts\activate
   ```
   
   **On macOS/Linux:**
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables**
   
   Copy the `.env.example` file to `.env`:
   ```bash
   cp .env.example .env
   ```
   
   Edit the `.env` file and add your OpenWeatherMap API key:
   ```
   OPENWEATHER_API_KEY=your_api_key_here
   ```

## Getting an OpenWeatherMap API Key

1. Visit [OpenWeatherMap](https://openweathermap.org/api)
2. Sign up for a free account
3. Go to your API keys section
4. Copy your default API key
5. Add it to your `.env` file

## Running the Application

1. Make sure your virtual environment is activated
2. Run the Flask app:
   ```bash
   python app.py
   ```
3. Open your browser and navigate to `http://localhost:5000`

## Project Structure

```
weather-dashboard/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── README.md             # This file
├── templates/
│   ├── index.html        # Main dashboard page
│   ├── 404.html          # 404 error page
│   └── 500.html          # 500 error page
└── static/
    ├── style.css         # CSS styles
    └── script.js         # JavaScript functionality
```

## API Endpoints

### GET `/`
Renders the main weather dashboard page for the default city (London).

### POST `/api/weather`
Fetches weather data for a specific city.

**Request:**
```json
{
  "city": "New York"
}
```

**Response:**
```json
{
  "weather": { /* current weather data */ },
  "forecast": [ /* 5-day forecast data */ ]
}
```

### GET `/api/cities`
Returns a list of preset cities for quick access.

## Customization

### Change Default City
Edit `app.py` and modify the `DEFAULT_CITY` variable:
```python
DEFAULT_CITY = 'Your City Here'
```

### Add More Quick Cities
Edit `app.py` in the `api_cities()` function:
```python
cities = ['London', 'New York', 'Tokyo', 'Your City', ...]
```

### Modify Temperature Units
By default, temperatures are shown in Celsius. To use Fahrenheit, change the API calls in `app.py`:
```python
url = f'{BASE_URL}/weather?q={city}&appid={API_KEY}&units=imperial'
```

## Deployment

### Heroku
1. Create a Procfile:
   ```
   web: gunicorn app:app
   ```

2. Create runtime.txt:
   ```
   python-3.10.0
   ```

3. Push to Heroku:
   ```bash
   heroku create your-app-name
   heroku config:set OPENWEATHER_API_KEY=your_api_key
   git push heroku main
   ```

### Docker
1. Create a Dockerfile
2. Build and run:
   ```bash
   docker build -t weather-dashboard .
   docker run -p 5000:5000 -e OPENWEATHER_API_KEY=your_key weather-dashboard
   ```

## Technologies Used

- **Backend**: Flask (Python web framework)
- **Frontend**: HTML5, CSS3, JavaScript
- **API**: OpenWeatherMap (free tier)
- **Icons**: Font Awesome
- **Styling**: Custom CSS with animations

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Troubleshooting

### API Key not working
- Make sure your API key is correctly added to the `.env` file
- Verify the API key is active on OpenWeatherMap
- Wait a few minutes after creating the API key for it to activate

### City not found
- Try searching with the city's English name
- Use city names like "London, UK" or "New York, US" for more specific results

### Application won't start
- Make sure all dependencies are installed: `pip install -r requirements.txt`
- Verify Python version is 3.8 or higher
- Check that port 5000 is not in use

## Support

If you encounter any issues, please open an issue on the GitHub repository.

## Future Enhancements

- [ ] User location detection
- [ ] Multiple city comparison
- [ ] Weather alerts
- [ ] Historical weather data
- [ ] Weather maps
- [ ] User preferences (temperature units, theme)
- [ ] Database to save favorite cities
- [ ] Mobile app

## Acknowledgments

- [OpenWeatherMap](https://openweathermap.org) for the weather data API
- [Font Awesome](https://fontawesome.com) for the icons
- [Flask](https://flask.palletsprojects.com) framework

---

**Happy coding! 🚀**
