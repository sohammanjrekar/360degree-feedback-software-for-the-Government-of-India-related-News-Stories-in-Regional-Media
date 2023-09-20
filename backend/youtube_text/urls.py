# youtube_data/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('api/fetch-youtube-data/', views.YouTubeVideoList.as_view(), name='fetch-youtube-data'),
]
