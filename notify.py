import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from twilio.rest import Client
from time import sleep

# Twilio Configuration
TWILIO_ACCOUNT_SID = 'AC73cd3cca1622fccc2ddef2478213638b'
TWILIO_AUTH_TOKEN = '08fd0f02de4872acee755058df5d1f20'
TWILIO_PHONE_NUMBER = '+12564748793'
RECIPIENT_PHONE_NUMBER = '+917045208474'

# Email Configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SMTP_EMAIL = 'sohammanjreKar@eng.rizvi.edu.in'
SMTP_PASSWORD = ''
RECIPIENT_EMAIL = 'mrsohammanjreKar@gmail.com'

def send_sms_notification():
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body='Negative story detected! Check your email for details.',
        from_=TWILIO_PHONE_NUMBER,
        to=RECIPIENT_PHONE_NUMBER
    )
    print('SMS sent:', message.sid)

def send_email_notification():
    msg = MIMEMultipart()
    msg['From'] = SMTP_EMAIL
    msg['To'] = RECIPIENT_EMAIL
    msg['Subject'] = 'Negative Story Alert'
    message = 'Negative story detected!'
    msg.attach(MIMEText(message, 'plain'))

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_EMAIL, SMTP_PASSWORD)
        server.sendmail(SMTP_EMAIL, RECIPIENT_EMAIL, msg.as_string())
    print('Email sent')
send_email_notification()