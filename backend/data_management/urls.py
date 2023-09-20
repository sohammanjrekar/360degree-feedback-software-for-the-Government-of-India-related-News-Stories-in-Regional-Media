# data_management/urls.py
from django.urls import path
from .views import NewsArticleListAPIView, VideoListAPIView, OCRTextListAPIView

urlpatterns = [
    path('api/news-articles/', NewsArticleListAPIView.as_view(), name='news-article-list'),
    path('api/videos/', VideoListAPIView.as_view(), name='video-list'),
    path('api/ocr-texts/', OCRTextListAPIView.as_view(), name='ocr-text-list'),
    # Implement URL patterns for other views as needed
]
