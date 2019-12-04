import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint

api_key = '19e11c06536b27688aa1202d7d040992'
base_url = "http://api.openweathermap.org/data/2.5/weather?"


def get_temperature(city_name):
    url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(url)
    res_json = response.json()
    current_temperature = round(res_json.get('main').get('temp') - 273, 1)
    return f'There is {current_temperature} degrees outside.'



def get_weather(city_name):
    url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(url)
    res_json = response.json()
    temp = round(res_json.get('main').get('temp') - 273, 1)
    temp_max = round(res_json.get('main').get('temp_max') - 273, 1)
    temp_min = round(res_json.get('main').get('temp_min') - 273, 1)
    cloudiness = res_json.get('clouds').get('all')
    humidity = res_json.get('main').get('humidity')
    pressure = res_json.get('main').get('pressure')
    description = res_json.get('weather')[0].get('description')

    return f'Temperature: {temp}.\
             Maximal temperature: {temp_max}.\
             Minimal temperature: {temp_min}.\
             Cloudiness: {cloudiness}%.\
             Humidity: {humidity}%.\
             Pressure: {pressure}.\
             There is {description}.'

