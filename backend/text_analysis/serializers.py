# text_analysis/serializers.py

from rest_framework import serializers
from .models import CategorizedArticle

class CategorizedArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategorizedArticle
        fields = '__all__'
