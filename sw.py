import requests
import json


cities = [
    {'name': 'Boston, MA', 'lat': '42.3601', 'lon': '-71.0589'},
    {'name': 'North Andover, MA', 'lat': '42.671970', 'lon': '-71.087440'},
    {'name': 'New York', 'lat': '40.7128', 'lon': '74.0060'},
    {'name': 'St. Johnsbury, VT', 'lat': '44.4193', 'lon': '-72.0151'},
    {'name': 'North Adams, MA', 'lat': '42.7009', 'lon': '-73.1087'}
]


# converts from kelvin to fahrenheit and returns rounded number
def convert_temp(temp):
    ftemp = round(((temp - 273.15) * 1.8) + 32, 1)
    return ftemp


def get_weather(lat, lon, name):
    key = 'API-KEY'
    apiCall = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={key}'
    response = requests.get(apiCall)
    weatherDataAll = json.loads(response.text)
    tempData = weatherDataAll['daily'][0]['temp']
    humidityData = weatherDataAll['daily'][0]['humidity']
    highTemp = convert_temp(tempData['max'])
    lowTemp = convert_temp(tempData['min'])

    return {'humidity': humidityData, "highTemp": highTemp, "lowTemp": lowTemp, "name": name}


for city in cities:
    get_weather_data = get_weather(city['lat'], city['lon'], city['name'])

    highTemp = get_weather_data['highTemp']
    lowTemp = get_weather_data['lowTemp']
    humidityData = get_weather_data['humidity']
    name = get_weather_data['name']

    print(f' Name: {name} \n Low: {lowTemp} \n High: {highTemp} \n Humidity: {humidityData} \n')
