# notification_app/utils.py

from twilio.rest import Client

def send_sms_notification(phone_number, message):
    account_sid = 'your_account_sid'
    auth_token = 'your_auth_token'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=message,
        from_='+1234567890',  # Your Twilio phone number
        to=phone_number
    )

    return message.sid
