from PIL import Image
import pytesseract
from googletrans import Translator
import re

# Path to the Tesseract executable (adjust as needed)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# List of languages to consider (Marathi, Urdu, Tamil, etc.)
languages = [
    "mar", "urd", "tam", "eng", "asm", "ben", "guj", "hin", "kan",
    "kas", "kok", "mal", "mni", "mar", "nep", "ori", "pan", "san",
    "snd", "tam", "tel", "urd", "bod", "sat", "mai", "dgo"
]  # ISO 639-2 language codes

def perform_ocr_and_translate(image_path):
    try:
        # Open the image using PIL
        image = Image.open(image_path)

        # Perform OCR and specify the language(s)
        recognized_text = pytesseract.image_to_string(image, lang="+".join(languages))

        # Initialize the Translator
        translator = Translator()

        # Translate the recognized text to English
        english_translation = translator.translate(recognized_text, src='auto', dest='en')

        return english_translation.text
    except Exception as e:
        return str(e)

def clean_text(text):
    # Define a regular expression pattern to remove non-alphanumeric characters
    pattern = re.compile(r'[^a-zA-Z0-9\s]+')

    # Use the pattern to replace unwanted characters with whitespace
    cleaned_text = re.sub(pattern, ' ', text)

    # Remove extra whitespace and trim the text
    cleaned_text = ' '.join(cleaned_text.split())

    return cleaned_text

if __name__ == "__main__":
    # Replace 'your_image.png' with the path to your image file
    image_path = 'news1.png'

    translated_text = perform_ocr_and_translate(image_path)

    # Clean the text
    cleaned_text = clean_text(translated_text)

    print("Recognized and Translated Text:")
    print(cleaned_text)

    # Save the cleaned response to a text file
    with open('output.txt', 'w', encoding='utf-8') as file:
        file.write(cleaned_text)

    print("Cleaned Response saved to 'output.txt'")
