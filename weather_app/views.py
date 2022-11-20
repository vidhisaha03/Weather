from django.shortcuts import render

# Create your views here.

import requests

def index(request):
    # https://openweathermap.org/  --Create an account here to get the api key
    # url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=API_KEY' -- we have to give the API_KEY
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=58f432f5834f2bde3087ab088e2c070d'

    city = 'Jamshedpur'

    city_weather = requests.get(url.format(city)).json() #we are requesting the API data and converting the JSON to Python data types
    print(city_weather) #checking the output
    weather = {
        'city' : city,
        'temperature' : city_weather['main']['temp'],
        'description' : city_weather['weather'][0]['description'],
        'icon' : city_weather['weather'][0]['icon'],
        'humidity' : city_weather['main']['humidity'],
        'pressure' : city_weather['main']['pressure'],
        'min_temp' : city_weather['main']['temp_min'],
        'max_temp' : city_weather['main']['temp_max']
    }

    city1 = 'Pune'
    city_weather1 = requests.get(url.format(city1)).json() #we are requesting the API data and converting the JSON to Python data types
    print(city_weather1) #checking the output
    weather1 = {
        'city' : city1,
        'temperature' : city_weather1['main']['temp'],
        'description' : city_weather1['weather'][0]['description'],
        'icon' : city_weather1['weather'][0]['icon'],
        'humidity' : city_weather1['main']['humidity'],
        'pressure' : city_weather1['main']['pressure'],
        'min_temp' : city_weather1['main']['temp_min'],
        'max_temp' : city_weather1['main']['temp_max']
    }

   

    return render(request, 'index.html', {'weather' : weather,'weather1': weather1}) #returns the index.html template

    
