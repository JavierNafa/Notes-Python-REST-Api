from os import getenv
from os.path import join
from pathlib import Path
from smtplib import SMTP
from email.utils import make_msgid
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

from_email = getenv('EMAIL_USER')
password = getenv('EMAIL_PASSWORD')
service = getenv('EMAIL_SERVICE')
port = getenv('EMAIL_PORT')


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
        with SMTP(host=service, port=port) as server:
            server.starttls()
            server.login(from_email, password)
            server.sendmail(from_email, to_email, body)
    except Exception as e:
        raise e


def attach_image(cid: str, image_name):
    try:
        file = join(Path().absolute(), f'src\\static\\images\\{image_name}')
        with open(file, 'rb') as fp:
            img = MIMEImage(fp.read())
            img.add_header('Content-ID', f'<{cid}>'.format(file))
            return img
    except Exception as e:
        raise e
