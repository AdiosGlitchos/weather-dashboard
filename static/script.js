// Format the update time
function updateTime() {
    const now = new Date();
    const timeString = now.toLocaleString('en-US', {
        year: 'numeric',
        month: 'short',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    });
    document.getElementById('updateTime').textContent = timeString;
}

// Load preset cities
async function loadCities() {
    try {
        const response = await fetch('/api/cities');
        const data = await response.json();
        const citiesList = document.getElementById('citiesList');
        
        citiesList.innerHTML = '';
        data.cities.forEach(city => {
            const btn = document.createElement('button');
            btn.className = 'city-btn';
            btn.textContent = city;
            btn.onclick = () => searchCity(city);
            citiesList.appendChild(btn);
        });
    } catch (error) {
        console.error('Error loading cities:', error);
    }
}

// Search for weather
async function searchCity(city = null) {
    const cityInput = document.getElementById('cityInput');
    const searchCity_name = city || cityInput.value.trim();
    
    if (!searchCity_name) {
        alert('Please enter a city name');
        return;
    }
    
    try {
        const response = await fetch('/api/weather', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ city: searchCity_name })
        });
        
        if (!response.ok) {
            alert('City not found. Please try another city.');
            return;
        }
        
        const data = await response.json();
        
        // Reload the page with new city data
        window.location.href = `/`;
        
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred while fetching weather data.');
    }
}

// Allow Enter key to search
document.addEventListener('DOMContentLoaded', () => {
    updateTime();
    loadCities();
    
    const cityInput = document.getElementById('cityInput');
    if (cityInput) {
        cityInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                searchCity();
            }
        });
    }
    
    // Update time every minute
    setInterval(updateTime, 60000);
});
