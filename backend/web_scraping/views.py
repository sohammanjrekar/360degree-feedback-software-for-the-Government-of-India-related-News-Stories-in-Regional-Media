from django.http import JsonResponse
from bs4 import BeautifulSoup
import requests







# web_scraping/views.py

from rest_framework import generics
from .models import ScrapedData
from .serializers import ScrapedDataSerializer

class ScrapedDataList(generics.ListCreateAPIView):
    queryset = ScrapedData.objects.all()
    serializer_class = ScrapedDataSerializer

    def perform_create(self, serializer):
        # Perform your web scraping here and save the data to the database
        scraped_data = scrape_news()
        # Then, save the scraped data using serializer.save()


def scrape_news(request):
    # Replace with the URL of a news website to scrape
    url = "https://example.com/news"

    # Perform the HTTP request and parse the HTML
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract relevant information (title, content, source, date)
    title = soup.find('h1').text
    content = soup.find('div', class_='article-content').text
    source = "Example News"
    publication_date = "2023-01-01"  # Replace with the actual publication date

    # Store the scraped data in the database
    news_article = NewsArticle(title=title, content=content, source=source, publication_date=publication_date)
    news_article.save()

    return JsonResponse({"message": "Scraped and saved successfully"})



