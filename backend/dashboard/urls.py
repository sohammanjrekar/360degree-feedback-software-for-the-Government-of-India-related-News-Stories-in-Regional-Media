# dashboard_app/urls.py
from django.urls import path
from .views import DashboardDataAPIView

urlpatterns = [
    path('api/dashboard-data/', DashboardDataAPIView.as_view(), name='dashboard-data'),
]
