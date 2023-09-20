from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    publication_date = models.DateField()
    video_id = models.CharField(max_length=50, unique=True)
