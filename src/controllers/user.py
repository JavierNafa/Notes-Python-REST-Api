from __future__ import absolute_import
from operator import itemgetter
from src.models.user import User
from src.tasks.mail import send
from src.utils import hash_generator, template_reader, mail_sender


def post_user(**props):
    try:
        name, last_name, email, password = itemgetter(
            'name', 'last_name', 'email', 'password')(props)
        user = User(name=name, last_name=last_name,
                    email=email)
        is_duplicated = user.count(email=email)
        if(is_duplicated >= 1):
            return {'success': False}
        hash = hash_generator.hash_password(password)
        user.hash = hash
        user.insert()
        send.apply_async(queue='high_priority', args=(
            'register', 'python', 'python.png', 'Register test', email), kwargs={'name': name.upper()})
        return {'success': True, 'data': {'name': name, 'last_name': last_name, 'email': email}}
    except Exception as e:
        raise e
