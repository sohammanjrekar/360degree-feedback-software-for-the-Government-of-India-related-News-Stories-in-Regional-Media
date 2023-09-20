# documentation_help/admin.py
from django.contrib import admin
from .models import DocumentationArticle, FAQ, UserGuide, SupportResource

admin.site.register(DocumentationArticle)
admin.site.register(FAQ)
admin.site.register(UserGuide)
admin.site.register(SupportResource)
