# notification_app/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import send_sms_notification

class NotificationAPIView(APIView):
    def post(self, request):
        data = request.data

        # Extract recipient phone number and message from data
        phone_number = data.get('phone_number')
        message = data.get('message')

        # Send the notification
        send_sms_notification(phone_number, message)

        return Response({'message': 'Notification sent successfully'})


