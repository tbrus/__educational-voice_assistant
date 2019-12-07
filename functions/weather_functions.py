import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint
import math

api_key = '19e11c06536b27688aa1202d7d040992'
base_url = "http://api.openweathermap.org/data/2.5/weather?"


def get_temperature(city_name):
    url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(url)
    res_json = response.json()
    current_temperature = round(res_json.get('main').get('temp') - 273)
    return f'Jest {current_temperature} stopni.'


def get_weather(city_name):
    url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(url)
    res_json = response.json()
    temp = round(res_json.get('main').get('temp') - 273)
    temp_max = round(res_json.get('main').get('temp_max') - 273)
    temp_min = round(res_json.get('main').get('temp_min') - 273)
    cloudiness = res_json.get('clouds').get('all')
    humidity = res_json.get('main').get('humidity')
    pressure = res_json.get('main').get('pressure')
    description = res_json.get('weather')[0].get('description')

    return f'Temperatura: {temp} stopni.\
             Maksymalna temperatura: {temp_max} stopni.\
             Minimalna temperatura: {temp_min} stopni.\
             Zachmurzenie: {cloudiness}%.\
             Wilgotność: {humidity}%.\
             Ciśnienie: {pressure} hektopaskali.'

