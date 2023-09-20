# ocr_app/views.py

from django.http import JsonResponse
import pytesseract
from PIL import Image

def perform_ocr(request):
    if request.method == 'POST':
        image = request.FILES['image']
        try:
            # Perform OCR on the uploaded image
            extracted_text = perform_ocr_on_image(image)

            # Create an OCRData object and save it to the database
            ocr_data = OCRData(image=image, extracted_text=extracted_text)
            ocr_data.save()

            return JsonResponse({'message': 'OCR performed successfully', 'text': extracted_text})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def perform_ocr_on_image(image):
    # Configure Tesseract as needed
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    
    # Perform OCR on the image
    img = Image.open(image)
    extracted_text = pytesseract.image_to_string(img)

    return extracted_text
