# settings_configuration/api.py
from rest_framework import serializers, viewsets
from .models import LanguagePreference

class LanguagePreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguagePreference
        fields = '__all__'

class LanguagePreferenceViewSet(viewsets.ModelViewSet):
    queryset = LanguagePreference.objects.all()
    serializer_class = LanguagePreferenceSerializer
