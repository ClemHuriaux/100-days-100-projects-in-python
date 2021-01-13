import os
from twilio.rest import Client
import smtplib

ACCOUNT_SID_TWILIO = "AC339ce8a07c8d1b1b410af0861d7e734e"
TWILIO_API_KEY = os.environ["TWILIO_API_KEY"]
NUM_TO_SEND = ""
MAIL_PASSWORD = os.environ["MAIL_PASSWORD"]
MAIL_USERNAME = os.environ["MAIL_USERNAME"]
MAIL_PROVIDER = "smtp.gmail.com"


class NotificationManager:

    def __init__(self):
        self.client = Client(ACCOUNT_SID_TWILIO, TWILIO_API_KEY)

    def send_sms(self, message):
        message = self.client.messages.create(
            to=NUM_TO_SEND,  # The num you want
            from_="+14158516224",
            body=message)
        print(message.sid)

    @staticmethod
    def send_emails(emails, message, google_flight_link):
        with smtplib.SMTP_SSL(MAIL_PROVIDER) as connection:
            connection.login(MAIL_USERNAME, MAIL_PASSWORD)
            for email in emails:
                print("sending mail to ", email)
                connection.sendmail(
                    from_addr=MAIL_USERNAME,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )


