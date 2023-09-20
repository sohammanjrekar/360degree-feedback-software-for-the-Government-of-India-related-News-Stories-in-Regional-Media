import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download("vader_lexicon")
# text_analysis/views.py

from rest_framework import generics
from .models import CategorizedArticle
from .serializers import CategorizedArticleSerializer

class CategorizedArticleList(generics.ListCreateAPIView):
    queryset = CategorizedArticle.objects.all()
    serializer_class = CategorizedArticleSerializer

    def perform_create(self, serializer):
        # Perform text analysis logic here
        categorized_data = perform_text_analysis()
        # Then, save the analyzed data using serializer.save()
def analyze_sentiment(request, text):
    analyzer = SentimentIntensityAnalyzer()
    sentiment_scores = analyzer.polarity_scores(text)

     # Determine the sentiment
    sentiment = "positive" if sentiment_scores["compound"] > 0 else "negative" if sentiment_scores["compound"] < 0 else "neutral"

    return JsonResponse({"sentiment": sentiment, "scores": sentiment_scores})
