import speech_recognition as sr
import pyaudio

def speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)

        print("Say something: Listening to your voice...")

        audio = recognizer.listen(source)

        text = recognizer.recognize_google(audio)
        print("You said:", text.capitalize())

speech_to_text()
