from googletrans import Translator, LANGUAGES

def translate_text(text, target_language):
    translator = Translator()
    try:
        translation = translator.translate(text, dest=target_language)
        return translation.text
    except Exception as e:
        print(f"Error during translation: {e}")
        return "Translation Error"

if __name__ == "__main__":
    print("Available Languages:")
    for code, name in LANGUAGES.items():
        print(f"{code}: {name}")

    text = input("Enter text to translate: ")
    target_language = input("Enter target language code: ")
    translated_text = translate_text(text, target_language)
    print(f"Translated Text: {translated_text}")
