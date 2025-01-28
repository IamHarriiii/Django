from django.shortcuts import render
from django.contrib import messages
import requests
import datetime
from django.conf import settings
from typing import Dict, Any

def get_weather_data(city: str) -> Dict[str, Any]:
    """Fetch weather data from OpenWeatherMap API"""
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'units': 'metric',
        'appid': settings.WEATHER_API_KEY
    }
    return requests.get(base_url, params=params).json()

def get_background_image(city: str) -> str:
    """Fetch high-quality city background image from Google Custom Search API"""
    params = {
        'key': settings.GOOGLE_API_KEY,
        'cx': settings.SEARCH_ENGINE_ID,
        'q': f"{city} cityscape panorama 4k",  # Updated search query for better quality
        'searchType': 'image',
        'imgSize': 'xlarge',
        'num': 1,
        'imgType': 'photo',  # Specifically request photos
        'rights': 'cc_publicdomain'  # Use public domain images for better quality
    }
    response = requests.get(
        'https://www.googleapis.com/customsearch/v1',
        params=params
    ).json()
    return response.get('items', [{}])[0].get('link', '')

def get_weather_context(city: str) -> Dict[str, Any]:
    """Get weather data and prepare context"""
    try:
        weather_data = get_weather_data(city)
        context = {
            'city': city,
            'description': weather_data['weather'][0]['description'],
            'icon': weather_data['weather'][0]['icon'],
            'temp': round(weather_data['main']['temp']),
            'humidity': weather_data['main']['humidity'],
            'wind_speed': round(weather_data['wind']['speed'], 1),
            'day': datetime.date.today(),
            'exception_occurred': False,
        }
        
        try:
            context['image_url'] = get_background_image(city)
        except Exception:
            # Use a high-quality default background
            context['image_url'] = 'https://images.pexels.com/photos/1034662/pexels-photo-1034662.jpeg'
            
        return context
    except Exception as e:
        return {
            'exception_occurred': True,
            'city': city,
            'description': 'clear sky',
            'icon': '01d',
            'temp': 20,
            'humidity': 60,
            'wind_speed': 5,
            'day': datetime.date.today(),
            'image_url': 'https://images.pexels.com/photos/1034662/pexels-photo-1034662.jpeg'
        }

def home(request):
    """View function for the weather dashboard"""
    if request.method == 'POST':
        city = request.POST.get('city', '').strip()
        if not city:
            messages.error(request, 'Please enter a city name')
            city = 'London'  # Fallback to London if empty
    else:
        city = 'London'  # Default city
    
    context = get_weather_context(city)
    return render(request, 'weather/index.html', context)