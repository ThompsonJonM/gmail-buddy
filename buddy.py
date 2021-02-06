import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from credentials import user


def send_email(recipient, subject, body) -> None:
    """Send an email using a Gmail address.
    
    :param recipient: The intended email recipient
    :param subject: The subject of the intended email
    :param body: The body of the intended email
    """
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = user['username']
    password = user['password']

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient
    message['Subject'] = subject
    body = MIMEText(body) 
    message.attach(body)

    server = smtplib.SMTP_SSL(smtp_server, port)
    server.login(sender_email, password)
    server.sendmail(sender_email, recipient, message.as_string())
    server.quit()
