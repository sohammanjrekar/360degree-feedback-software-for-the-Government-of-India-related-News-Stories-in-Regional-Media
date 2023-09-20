# ocr_app/models.py

from django.db import models

class OCRData(models.Model):
    image = models.ImageField(upload_to='ocr_images/')
    extracted_text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'OCR Data #{self.id}'
