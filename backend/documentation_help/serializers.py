# documentation_help/api.py
from rest_framework import serializers, viewsets
from .models import DocumentationArticle, FAQ, UserGuide, SupportResource

class DocumentationArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentationArticle
        fields = '__all__'

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'

class UserGuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGuide
        fields = '__all__'

class SupportResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportResource
        fields = '__all__'

class DocumentationArticleViewSet(viewsets.ModelViewSet):
    queryset = DocumentationArticle.objects.all()
    serializer_class = DocumentationArticleSerializer

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

class UserGuideViewSet(viewsets.ModelViewSet):
    queryset = UserGuide.objects.all()
    serializer_class = UserGuideSerializer

class SupportResourceViewSet(viewsets.ModelViewSet):
    queryset = SupportResource.objects.all()
    serializer_class = SupportResourceSerializer
