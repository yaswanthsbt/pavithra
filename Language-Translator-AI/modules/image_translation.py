import cv2
import pytesseract
from googletrans import Translator

def image_to_text(image_path, target_language='en'):
    try:
        # Read the image using OpenCV
        img = cv2.imread(image_path)
        
        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Perform OCR using Pytesseract
        extracted_text = pytesseract.image_to_string(gray)
        print(f"Extracted Text: {extracted_text}")
        
        # Translate the text using Google Translator
        translator = Translator()
        translated_text = translator.translate(extracted_text, dest=target_language)
        print(f"Translated Text ({target_language}): {translated_text.text}")
        
        return translated_text.text
    except Exception as e:
        print(f"Error in image translation: {e}")
        return None

if __name__ == "__main__":
    image_path = input("Enter the path of the image: ")
    target_language = input("Enter target language code (e.g., 'en' for English, 'fr' for French): ")
    image_to_text(image_path, target_language)
