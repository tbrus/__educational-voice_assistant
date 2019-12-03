import os
import datetime
from functions.main_functions import speak, get_audio
from functions.simple_functions import get_time

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
                        if 'time' in text:
                            speak(get_time())

                        # Sleep
                        if 'sleep' in text:
                            print('gonna sleep')
                            break


                        # When everything during request is done
                        speak('What else can I do for you?')


                    # If don't understand
                    else:
                        speak('I don\'t understand. Could you repeat?')



# REPAIR EXCEPTION TO TRY AGAIN IF EX DOES NOT UNDERSTAND
# ADD FUNCIONALITIES


