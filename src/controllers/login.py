from src.models.user import User
from src.utils.token_generator import generate_token


def post_login(user_id):
    try:
        token = generate_token(user_id)
        return token
    except Exception as e:
        raise e
