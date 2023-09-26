# Your project's urls.py
from django.contrib import admin
from django.urls import path, include  # Import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ocr/', include('ocr.urls')),  # Include your app's URLs
]
