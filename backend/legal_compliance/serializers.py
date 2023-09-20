# legal_compliance/api.py
from rest_framework import serializers, viewsets
from .models import PrivacyPolicy, TermsOfUse, CookiePolicy

class PrivacyPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivacyPolicy
        fields = '__all__'

class TermsOfUseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TermsOfUse
        fields = '__all__'

class CookiePolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = CookiePolicy
        fields = '__all__'

class PrivacyPolicyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PrivacyPolicy.objects.all()
    serializer_class = PrivacyPolicySerializer

class TermsOfUseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TermsOfUse.objects.all()
    serializer_class = TermsOfUseSerializer

class CookiePolicyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CookiePolicy.objects.all()
    serializer_class = CookiePolicySerializer
