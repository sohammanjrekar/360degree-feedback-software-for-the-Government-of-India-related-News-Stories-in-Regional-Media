# text_analysis/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('api/analyze-sentiment/', views.CategorizedArticleList.as_view(), name='analyze-sentiment'),
]
