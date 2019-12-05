import webbrowser
import requests
import re

def search_youtube(text):
    query = text.split('youtube for ')[-1]
    url = 'https://www.youtube.com/results?search_query=' + query
    webbrowser.open(url)


def search_google(text):
    query = text.split('google for ')[-1]
    url = 'https://www.google.com/search?q=' + query
    webbrowser.open(url)


def search_wikipedia(text):
    query = text.split('wikipedia for ')[-1]
    url = 'https://www.wikipedia.com/wiki/' + query
    webbrowser.open(url)


def play_first_youtube(text):
    query = text.split('play ')[-1]
    url = 'https://www.youtube.com/results?search_query=' + query
    response = requests.get(url).text

    search_response = re.findall(r'href=\"\/watch\?v=(.{11})', response)
    video_url = 'https://www.youtube.com/watch?v=' + search_response[0]

    webbrowser.open(video_url)


def play_nth_youtube(text, n):
    query = text.split('youtube for ')[-1]
    url = 'https://www.youtube.com/results?search_query=' + query
    response = requests.get(url).text

    search_response = re.findall(r'href=\"\/watch\?v=(.{11})', response)
    search = list(dict.fromkeys(search_response))

    video_url = 'https://www.youtube.com/watch?v=' + search[n]

    webbrowser.open(video_url)


# def open_google_results(text, n):
#     query = text.split('google for ')[-1]
#     url = 'https://www.google.com/search?q=' + query
#     response = requests.get(url).text
#     print(url)

#     search_response = re.findall('http.?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', response)
#     search = list(dict.fromkeys(search_response))
#     print(search)
#     go_to_url = search[n]
#     print(go_to_url)
#     webbrowser.open(go_to_url)

#     webbrowser.open(url)

# open_google_results('search google for pandas python', 1)
