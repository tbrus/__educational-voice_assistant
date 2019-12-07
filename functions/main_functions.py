import speech_recognition as sr
from gtts import gTTS
import pygame
from pygame import mixer
from time import sleep


def speak(text):
    text_to_speech = gTTS(text=text, lang="pl")
    filename = "audio.mp3"
    text_to_speech.save(filename)

    mixer.init()
    mixer.music.load(filename)
    mixer.music.play()
    while pygame.mixer.music.get_busy():
        sleep(0.1)


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.energy_threshold = 2000
        r.dynamic_energy_threshold = True
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source, timeout=15)

        try:
            sentence = r.recognize_google(audio, language="pl-PL")
            print(sentence.lower())
            return sentence.lower()

        except sr.UnknownValueError:
            pass

        except sr.RequestError:
            pass

