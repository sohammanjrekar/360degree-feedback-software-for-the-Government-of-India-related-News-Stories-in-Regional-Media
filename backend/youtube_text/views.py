from django.http import JsonResponse
from googleapiclient.discovery import build
# youtube_data/views.py

from rest_framework import generics
from .models import YouTubeVideo
from .serializers import YouTubeVideoSerializer

class YouTubeVideoList(generics.ListCreateAPIView):
    queryset = YouTubeVideo.objects.all()
    serializer_class = YouTubeVideoSerializer

    def perform_create(self, serializer):
        # Perform the logic to fetch YouTube data here
        youtube_data = fetch_youtube_data()
        # Then, save the fetched data using serializer.save()


def fetch_youtube_data(request):
    # Replace with your YouTube API credentials
    api_key = "YOUR_API_KEY"
    youtube = build("youtube", "v3", developerKey=api_key)

    # Replace with your desired search parameters
    search_query = "Government of India"

    # Perform a search using the YouTube API
    search_response = youtube.search().list(
        q=search_query,
        type="video",
        part="id",
        maxResults=10  # Adjust as needed
    ).execute()

    # Extract video data
    videos = []
    for search_result in search_response.get("items", []):
        video_id = search_result["id"]["videoId"]
        video_data = youtube.videos().list(
            id=video_id,
            part="snippet"
        ).execute()
        video = video_data["items"][0]
        videos.append({
            "title": video["snippet"]["title"],
            "description": video["snippet"]["description"],
            "publication_date": video["snippet"]["publishedAt"],
            "video_id": video_id
        })

    # Store the retrieved video data in the database
    for video in videos:
        Video.objects.create(**video)

    return JsonResponse({"message": "YouTube data fetched and saved successfully"})
