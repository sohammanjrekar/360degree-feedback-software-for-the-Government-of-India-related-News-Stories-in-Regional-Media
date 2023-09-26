# ocr_translation/views.py
import pytesseract
from googletrans import Translator
import re
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Path to the Tesseract executable (adjust as needed)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# List of languages to consider (Marathi, Urdu, Tamil, etc.)
languages = [
    "mar", "urd", "tam", "eng", "asm", "ben", "guj", "hin", "kan",
    "kas", "kok", "mal", "mni", "mar", "nep", "ori", "pan", "san",
    "snd", "tam", "tel", "urd", "bod", "sat", "mai", "dgo"
]  # ISO 639-2 language codes

@csrf_exempt
def ocr_translation_view(request):
    if request.method == 'POST' and request.FILES.get('image'):
        try:
            # Open the image using PIL
            image = Image.open(request.FILES['image'])

            # Perform OCR and specify the language(s)
            recognized_text = pytesseract.image_to_string(image, lang="+".join(languages))

            # Initialize the Translator
            translator = Translator()

            # Translate the recognized text to English
            english_translation = translator.translate(recognized_text, src='auto', dest='en')

            # Clean the text
            cleaned_text = clean_text(english_translation.text)

            return JsonResponse({'cleaned_text': cleaned_text})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)

def clean_text(text):
    # Define a regular expression pattern to remove non-alphanumeric characters
    pattern = re.compile(r'[^a-zA-Z0-9\s]+')

    # Use the pattern to replace unwanted characters with whitespace
    cleaned_text = re.sub(pattern, ' ', text)

    # Remove extra whitespace and trim the text
    cleaned_text = ' '.join(cleaned_text.split())

    return cleaned_text
