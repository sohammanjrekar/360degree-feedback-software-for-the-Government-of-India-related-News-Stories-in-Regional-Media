# data_management/admin.py
from django.contrib import admin
from .models import NewsArticle, Video, OCRText

admin.site.register(NewsArticle)
admin.site.register(Video)
admin.site.register(OCRText)
