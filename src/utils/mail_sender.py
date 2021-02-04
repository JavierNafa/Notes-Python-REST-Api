from os.path import join
from pathlib import Path
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from settings import email_port, email_service, from_email, email_password


def create_mail(to_email: str, subject: str, template, attachment):
    try:
        message = MIMEMultipart()
        message['Subject'] = subject
        message['From'] = from_email
        message['To'] = to_email

        message.attach(MIMEText(template, 'html'))
        message.attach(attachment)
        body = message.as_string()
        return body
    except Exception as e:
        raise e


def send_mail(to_email, body):
    try:
        with SMTP(host=email_service, port=email_port) as server:
            server.starttls()
            server.login(from_email, email_password)
            server.sendmail(from_email, to_email, body)
    except Exception as e:
        raise e


def attach_image(cid: str, image_name):
    try:
        file = join(Path().absolute(), f'src/static/images/{image_name}')
        with open(file, 'rb') as fp:
            img = MIMEImage(fp.read())
            img.add_header('Content-ID', f'<{cid}>'.format(file))
            return img
    except Exception as e:
        raise e
