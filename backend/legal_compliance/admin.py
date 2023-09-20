# legal_compliance/admin.py
from django.contrib import admin
from .models import PrivacyPolicy, TermsOfUse

admin.site.register(PrivacyPolicy)
admin.site.register(TermsOfUse)
