# documentation_help/models.py
from django.db import models

class DocumentationArticle(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=100)
    tags = models.ManyToManyField('Tag')

class FAQ(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()

class UserGuide(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

class SupportResource(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='support_resources/')
