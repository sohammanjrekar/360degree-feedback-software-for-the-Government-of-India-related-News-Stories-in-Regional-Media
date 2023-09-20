# notification_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('api/notifications/', views.NotificationAPIView.as_view(), name='send-notification'),
]
