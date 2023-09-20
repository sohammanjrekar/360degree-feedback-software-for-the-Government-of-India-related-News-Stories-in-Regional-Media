# dashboard_app/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import NewsArticle, Video
from .serializers import NewsArticleSerializer, VideoSerializer

class DashboardDataAPIView(APIView):
    def get(self, request):
        # Retrieve data from models
        news_articles = NewsArticle.objects.all()
        videos = Video.objects.all()

        # Serialize data
        news_serializer = NewsArticleSerializer(news_articles, many=True)
        video_serializer = VideoSerializer(videos, many=True)

        # Return serialized data as JSON
        return Response({
            'news_articles': news_serializer.data,
            'videos': video_serializer.data,
        })
