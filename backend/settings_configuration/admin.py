# settings_configuration/admin.py
from django.contrib import admin
from .models import LanguagePreference

admin.site.register(LanguagePreference)
