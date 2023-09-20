from rest_framework import generics
from .models import NewsArticle, Video, OCRText
from .serializers import NewsArticleSerializer, VideoSerializer, OCRTextSerializer

# View for retrieving a list of news articles
class NewsArticleListAPIView(generics.ListAPIView):
    queryset = NewsArticle.objects.all()
    serializer_class = NewsArticleSerializer

# View for retrieving a list of videos
class VideoListAPIView(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

# View for retrieving a list of OCRText entries
class OCRTextListAPIView(generics.ListAPIView):
    queryset = OCRText.objects.all()
    serializer_class = OCRTextSerializer
