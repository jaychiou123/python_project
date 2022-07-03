from twilio.rest import Client

TWILIO_SID = "ACda0e3734fa670ae18b8441cf6f81b4a0"
TWILIO_AUTH_TOKEN = "9ac40e0b6883ee2fda12a1ae727c7996"
TWILIO_VIRTUAL_NUMBER = "+13512000611"
TWILIO_VERIFIED_NUMBER = "+886939862682"
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )