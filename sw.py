import requests
import json


# Place all city names in text file names cities.txt
file = open('cities.txt', 'r')

data = file.readlines()
cities = []
high_temp_list = []

for i in data:
    cities.append(i.strip())


# converts from kelvin to fahrenheit and returns rounded number
def convert_temp(temp):
    ftemp = round(((temp - 273.15) * 1.8) + 32, 1)
    return ftemp

# Uses opencagedata.com to convert city names into long and lat.
def get_coords(city_name):
    key = 'API_KEY'
    api_call = f'https://api.opencagedata.com/geocode/v1/json?q={city_name}&key={key}'

    response = requests.get(api_call)
    location_data = json.loads(response.text)

    city_name = location_data['results'][0]['formatted']
    lat = location_data['results'][0]['bounds']['northeast']['lat']
    lon = location_data['results'][0]['bounds']['northeast']['lng']

    return{'lat': lat, 'lon': lon, 'city_name': city_name}


# Uses openweathermap.com to the data received from get_coords to weather data.
def get_weather(lat, lon, city_name):
    key = 'API_KEY'
    apiCall = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={key}'
    response = requests.get(apiCall)
    weatherDataAll = json.loads(response.text)
    tempData = weatherDataAll['daily'][0]['temp']
    humidityData = weatherDataAll['daily'][0]['humidity']
    highTemp = convert_temp(tempData['max'])
    lowTemp = convert_temp(tempData['min'])

    return {'humidity': humidityData, "highTemp": highTemp, "lowTemp": lowTemp, "city_name": city_name}


# Goes through list of cities, converts city names to long and lat then pulls weather data.
for city in cities:
    city_data = get_coords(city)
    get_weather_data = get_weather(city_data['lat'], city_data['lon'], city_data['city_name'])
    highTemp = get_weather_data['highTemp']
    lowTemp = get_weather_data['lowTemp']
    humidityData = get_weather_data['humidity']
    city_name = get_weather_data['city_name']

    print(f' Name: {city_name} \n Low: {lowTemp} \n High: {highTemp} \n Humidity: {humidityData} \n')

    high_temp_list.append((city_name, highTemp))

high_temp_list.sort(key=lambda x: x[1])


hottest_city, hottest_temp = high_temp_list[-1]
coolest_city, coolest_temp = high_temp_list[0]

print(f' The hottest city in the US is {hottest_city} at {hottest_temp}')
print(f' The coolest city in the US is {coolest_city} at {coolest_temp}')
