from django.shortcuts import render, redirect
import requests
import urllib.request



# Create your views here.
def home_page(request):
    
    city = ''
    weather_data = {}

    if request.method == 'POST':
        city = request.POST.get('city')
        api_key = ''
        url = (f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric')
        
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()

            weather_data = {
                "country_code" : data["sys"]["country"],
                "condition" : data["weather"][0]["main"],
                "temperature" : data["main"]["temp"],
                "coordinate": str(data["coord"]["lon"]) + ' ' + str(data["coord"]["lat"]),
                "humidity" : data["main"]["humidity"],
                "presure" : data["main"]["pressure"]
            }
        else:
            weather_data["error"] = 'City Not Found'  
    
    return render(request, template_name='index.html', context={'city':city, 'weather_data':weather_data})