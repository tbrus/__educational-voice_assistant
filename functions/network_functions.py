from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import webbrowser
from bs4 import BeautifulSoup
import requests
import pprint
import re

def search_youtube(text):
    query = text.split('for ')[-1]
    url = 'https://www.youtube.com/results?search_query=' + query
    webbrowser.open(url)


def search_google(text):
    query = text.split('for ')[-1]
    url = 'https://www.google.com/search?q=' + query
    webbrowser.open(url)


def search_wikipedia(text):
    query = text.split('for ')[-1]
    url = 'https://www.wikipedia.com/wiki/' + query
    webbrowser.open(url)


def play_first_youtube(text):
    query = text.split('play ')[-1]
    url = 'https://www.youtube.com/results?search_query=' + query
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'lxml')

    search_response = re.findall(r'href=\"\/watch\?v=(.{11})', response)
    video_url = 'https://www.youtube.com/watch?v=' + search_response[0]

    webbrowser.open(video_url)


# def search_google(text):
#     url = 'https://www.google.com/'

#     driver = webdriver.Chrome(executable_path=r"/home/tomek/Desktop/voice_assistant/voice_assistant/chromedriver")
#     driver.implicitly_wait(1)
#     driver.maximize_window()

#     driver.get(url)
#     search = browser.find_element_by_name('q')
#     search.send_keys(str())
#     search.send_keys(Keys.RETURN)
