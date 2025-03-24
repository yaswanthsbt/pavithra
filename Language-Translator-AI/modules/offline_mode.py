# modules/offline_mode.py

import speech_recognition as sr

def offline_speech_recognition():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak something...")
        try:
            audio = recognizer.listen(source)
            print("Recognizing...")
            text = recognizer.recognize_sphinx(audio)  # Using Sphinx for offline recognition
            return text
        except Exception as e:
            return f"Error during recognition: {e}"
