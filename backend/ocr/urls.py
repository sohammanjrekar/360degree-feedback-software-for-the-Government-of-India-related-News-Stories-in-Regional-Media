# ocr_translation/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('ocr-translation/', views.ocr_translation_view, name='ocr-translation'),
]
