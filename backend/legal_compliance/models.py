# legal_compliance/models.py
from django.db import models
from django.conf import settings
class PrivacyPolicy(models.Model):
    content = models.TextField()
    version = models.CharField(max_length=20)
    publication_date = models.DateField(auto_now_add=True)

class TermsOfUse(models.Model):
    content = models.TextField()
    version = models.CharField(max_length=20)
    publication_date = models.DateField(auto_now_add=True)
class UserConsent(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    privacy_policy = models.ForeignKey(PrivacyPolicy, on_delete=models.CASCADE)
    terms_of_use = models.ForeignKey(TermsOfUse, on_delete=models.CASCADE)
    consent_date = models.DateTimeField(auto_now_add=True)
class CookiePolicy(models.Model):
    content = models.TextField()
    version = models.CharField(max_length=20)
    publication_date = models.DateField(auto_now_add=True)

class UserCookieConsent(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cookie_policy = models.ForeignKey(CookiePolicy, on_delete=models.CASCADE)
    consent_date = models.DateTimeField(auto_now_add=True)