import os
import datetime
from functions.main_functions import speak, get_audio
from functions.simple_functions import get_time, get_today_date
from functions.weather_functions import get_temperature, get_weather

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

                        # Sleep
                        elif 'sleep' in text:
                            print('gonna sleep')
                            break

                        # When everything during request is done



                    # If don't understand
                    else:
                        speak('I don\'t understand. Could you repeat?')



# REPAIR EXCEPTION TO TRY AGAIN IF EX DOES NOT UNDERSTAND
# ADD FUNCIONALITIES


