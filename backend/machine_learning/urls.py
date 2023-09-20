# ml_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('api/predict-ml/', views.predict_with_ml_model, name='predict-ml'),
]
