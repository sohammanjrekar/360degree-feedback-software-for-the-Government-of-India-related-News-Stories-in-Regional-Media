# web_scraping/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('api/scrape-news/', views.ScrapedDataList.as_view(), name='scrape-news'),
]
