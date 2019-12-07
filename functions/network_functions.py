import webbrowser
import requests
import re
import os
import smtplib


def search_youtube(text):
    if 'youtube' in text:
        query = text.split('youtube ')[-1]
    elif 'youtubie' in text:
        query = text.split('youtubie ')[-1]
    url = 'https://www.youtube.com/results?search_query=' + query
    webbrowser.open(url)


def search_google(text):
    query = text.split('google ')[-1]
    url = 'https://www.google.com/search?q=' + query
    webbrowser.open(url)


def search_wikipedia(text):
    if 'wikipedia' in text:
        query = text.split('wikipedia ')[-1]
    elif 'wikipedii' in text:
        query = text.split('wikipedii ')[-1]
    url = 'https://www.wikipedia.com/wiki/' + query
    webbrowser.open(url)


def play_first_youtube(text):
    if 'puść' in text:
        query = text.split('puść ')[-1]
    elif 'włącz' in text:
        query = text.split('włącz ')[-1]
    url = 'https://www.youtube.com/results?search_query=' + query
    response = requests.get(url).text

    search_response = re.findall(r'href=\"\/watch\?v=(.{11})', response)
    video_url = 'https://www.youtube.com/watch?v=' + search_response[0]

    webbrowser.open(video_url)


def play_nth_youtube(text, n):
    if 'youtube' in text:
        query = text.split('youtube ')[-1]
    elif 'youtubie' in text:
        query = text.split('youtubie ')[-1]
    url = 'https://www.youtube.com/results?search_query=' + query
    response = requests.get(url).text

    search_response = re.findall(r'href=\"\/watch\?v=(.{11})', response)
    search = list(dict.fromkeys(search_response))

    video_url = 'https://www.youtube.com/watch?v=' + search[n]

    webbrowser.open(video_url)


def create_email(login, receiver, subject, message):
    subject = subject[0].upper() + subject[1:]
    message = message[0].upper() + message[1:]

    content = f"""\
FROM: {login}
TO: {receiver}
SUBJECT: {subject}

{message}
"""
    print('\n\n', content)

    return content


def send_email(login, password, receiver, content):
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()

    mail.login(login, password)
    mail.sendmail(login, receiver, content.encode('UTF-8'))
    mail.close()
