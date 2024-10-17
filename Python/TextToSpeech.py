import pyttsx3
import speech_recognition as sr
def TextToSpeech():
    text = input("Enter the text which you want to be converted in speech: ")
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
TextToSpeech()
