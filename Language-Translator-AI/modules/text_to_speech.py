from gtts import gTTS
import os

def text_to_speech(text, lang='en', gender='male'):
    try:
        if gender == 'male':
            tts = gTTS(text=text, lang=lang, slow=False)
        else:
            print("Note: gTTS only provides female voices. Using default voice.")
            tts = gTTS(text=text, lang=lang, slow=False)
        
        tts.save("output.mp3")
        os.system("start output.mp3" if os.name == 'nt' else "afplay output.mp3")
        print("Audio played successfully.")
    except Exception as e:
        print(f"Error during Text-to-Speech: {e}")

if __name__ == "__main__":
    text = input("Enter text to convert to speech: ")
    lang = input("Enter language code (e.g., 'en' for English, 'fr' for French): ")
    gender = input("Enter preferred gender (male/female): ")
    text_to_speech(text, lang, gender)