from operator import itemgetter
from src.models.user import User
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
        template = template_reader.read_template(
            template_name='register', name=name)
        image = mail_sender.attach_image('python', 'python.png')
        body = mail_sender.create_mail(email, 'Register test', template, image)
        mail_sender.send_mail(email, body)
        return {'success': True, 'data': {'name': name, 'last_name': last_name, 'email': email}}
    except Exception as e:
        raise e
