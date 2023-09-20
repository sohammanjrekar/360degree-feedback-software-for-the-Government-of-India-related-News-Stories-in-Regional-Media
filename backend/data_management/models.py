# data_management/models.py
from django.db import models

class NewsArticle(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    # Add other fields as needed
    ...

class Video(models.Model):
    title = models.CharField(max_length=200)
    video_url = models.URLField()
    # Add other fields as needed
    ...

class OCRText(models.Model):
    text = models.TextField()
    source = models.ForeignKey(NewsArticle, on_delete=models.CASCADE)
    # Add other fields as needed
    ...
