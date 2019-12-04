import os
import datetime
from functions.main_functions import speak, get_audio
from functions.simple_functions import get_time, get_today_date
from functions.weather_functions import get_temperature, get_weather
from functions.network_functions import search_youtube, search_google, search_wikipedia, play_first_youtube
import webbrowser

feelings = ['how are you', 'how\'s it going', 'how is it going', 'what about you', 'how about you']
greetings = ['hi', 'hello', 'hey', 'good morning', 'good afternoon']



if __name__ == '__main__':

    speak('Hello Tom!')

    while True:
        text = get_audio()

        if text != None:
            if 'wake up' in text:
                speak('I\'m ready.')

                while True:
                    text = get_audio()
                    if text != None:

                        # Greetings
                        for greeting in greetings:
                            if greeting in text:
                                speak('Hello, how are you?')

                        # Feelings
                        for phrase in feelings:
                            if phrase in text:
                                speak('I\'m good as always, thank you.')

                        # Thanks
                        if 'thanks' in text or 'thank you' in text:
                            speak('You\'re welcome.')

                        # Time
                        if 'time' in text and 'what' in text:
                            speak(get_time())
                            speak('What else can I do for you?')

                        # Date Today
                        elif 'date' in text and 'today' in text:
                            speak(get_today_date())
                            speak('What else can I do for you?')

                         # Get current temperature
                        elif 'what' in text and 'temperature' in text:
                            speak(get_temperature('Warsaw'))
                            speak('What else can I do for you?')

                         # Get current temperature
                        elif 'what' in text and 'weather' in text:
                            speak(get_weather('Warsaw'))
                            speak('What else can I do for you?')


                # OPEN NETWORK SITES

                        # Open Google
                        elif 'open google' in text:
                            webbrowser.open('https://www.google.com/', new=2)
                            speak('What else can I do for you?')

                        # Open Youtube
                        elif 'open youtube' in text:
                            webbrowser.open('https://www.youtube.com/', new=2)
                            speak('What else can I do for you?')

                        # Open Gmail
                        elif 'open mail' in text or 'open email' in text or 'open gmail' in text:
                            webbrowser.open('https://www.gmail.com/', new=2)
                            speak('What else can I do for you?')

                        # Open Facebook
                        elif 'open facebook' in text:
                            webbrowser.open('https://www.facebook.com/', new=2)
                            speak('What else can I do for you?')


                # SEARCH NETWORK SITES

                        # Search Youtube for smth
                        elif 'search youtube for' in text or 'youtube for' in text:
                            search_youtube(text)
                            speak('What else can I do for you?')

                        # Search Google for smth
                        elif 'search google for' in text or 'google for' in text:
                            search_google(text)
                            speak('What else can I do for you?')

                        # Search Wikipedia for smth
                        elif 'search wikipedia for' in text or 'wikipedia for' in text:
                            search_wikipedia(text)
                            speak('What else can I do for you?')


                # SEARCH GOOGLE AND OPEN

                        # Search Google and open first
                        # elif 'search google for' in text:
                        #     search_google(text)
                        #     speak('What else can I do for you?')


                # PLAY YOUTUBE SONG

                        # Play 1st result Youtube search
                        elif 'play' in text:
                            play_first_youtube(text)


                # MAIL

                        # Check mails and read headers and from who
                        # elif 'search youtube for' in text:
                        #     search_youtube(text)
                        #     speak('What else can I do for you?')

                        # Send mail
                        # elif 'search youtube for' in text:
                        #     search_youtube(text)
                        #     speak('What else can I do for you?')


                # SLEEP
                        # Sleep
                        elif 'sleep' in text:
                            print('gonna sleep')
                            break

                        # When everything during request is done



                        # If don't understand
                        else:
                            speak('I don\'t understand. Could you repeat?')
