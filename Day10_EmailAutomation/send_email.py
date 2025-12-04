import smtplib
from email.message import EmailMessage

SENDER = "DavidNwanolue05@gmail.com"
APP_PASSWORD = "Dave2005"
RECEIVER = "ngpea@yahoo.ie"

msg = EmailMessage()
msg["Subject"] = "Automated Email Test"
msg["From"] = SENDER
msg["To"] = RECEIVER
msg.set_content("Hello! This is an automated email sent from Python.")

def send_email():
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(SENDER, APP_PASSWORD)
        smtp.send_message(msg)
        print("Email sent successfully!")

send_email()
