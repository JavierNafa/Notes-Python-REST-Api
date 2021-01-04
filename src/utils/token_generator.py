from os import getenv
from jwt import encode, decode
from datetime import datetime, timedelta

secret_key = getenv('TOKEN_KEY')


def generate_token(user_id):
    try:
        token = encode({'user_id': user_id, 'exp': datetime.utcnow()
                        + timedelta(hours=1)}, secret_key, algorithm='HS256')
        return token.decode('utf-8')
    except Exception as e:
        raise e


def decode_token(token):
    try:
        decoded = decode(token, secret_key, algorithms=['HS256'])
        return decoded
    except Exception as e:
        raise e
