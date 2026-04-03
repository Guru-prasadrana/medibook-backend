import os
from twilio.rest import Client

ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE = os.getenv("TWILIO_PHONE")

client = Client(ACCOUNT_SID, AUTH_TOKEN)


def send_sms(phone: str, otp: str):
    message = client.messages.create(
        body=f"Your OTP is {otp}",
        from_=TWILIO_PHONE,
        to=f"+91{phone}"
    )
    return message.sid