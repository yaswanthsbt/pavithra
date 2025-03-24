import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak something...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio_data = recognizer.listen(source)
            print("Recognizing...")
            text = recognizer.recognize_google(audio_data)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, could not understand the audio.")
            return None
        except sr.RequestError:
            print("Could not request results, please check your internet connection.")
            return None

if __name__ == "__main__":
    recognized_text = recognize_speech()
    if recognized_text:
        print(f"Recognized Text: {recognized_text}")
