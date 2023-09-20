# dashboard_app/models.py
from django.db import models

class NewsArticle(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publication_date = models.DateField()

    def __str__(self):
        return self.title

class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    video_url = models.URLField()
    publication_date = models.DateField()

    def __str__(self):
        return self.title
