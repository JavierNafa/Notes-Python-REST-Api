from __future__ import absolute_import, unicode_literals
from celery_holder import celery
from src.utils import mail_sender, template_reader


@celery.task(name='src.tasks.mail.send', auto_retry=[Exception], max_retries=2)
def send(template_name: str, cid: str, image_name: str, subject: str, to: str, **template_params):
    try:
        template = template_reader.read_template(
            template_name=template_name, data=template_params)
        image = mail_sender.attach_image(cid, image_name)
        body = mail_sender.create_mail(to, subject, template, image)
        mail_sender.send_mail(to, body)
    except Exception as e:
        raise e
