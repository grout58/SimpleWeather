import requests
import json


# converts from kelvin to fahrenheit and returns rounded number
def convert_temp(temp):
    ftemp = round(((temp - 273.15) * 1.8) + 32, 1)
    return ftemp


key = 'API_KEY'
lat = '42.671970'
lon = '-71.087440'
apiCall = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={key}'
response = requests.get(apiCall)
weatherDataAll = json.loads(response.text)

tempData = weatherDataAll['daily'][0]['temp']
humidityData = weatherDataAll['daily'][0]['humidity']

highTemp = convert_temp(tempData['max'])
lowTemp = convert_temp(tempData['min'])

print(f' Low: {lowTemp} \n High: {highTemp} \n Humidity: {humidityData}')
