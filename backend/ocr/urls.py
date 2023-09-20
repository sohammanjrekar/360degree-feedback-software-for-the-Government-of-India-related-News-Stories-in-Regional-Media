# ocr_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('api/perform-ocr/', views.perform_ocr, name='perform-ocr'),
]
