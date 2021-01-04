from operator import itemgetter
from src.models.user import User
from bson.objectid import ObjectId
from flask import request, g, redirect
from src.utils import token_generator, hash_generator, response_error


def verify_user():
    try:
        body = request.json.copy()
        email, password = itemgetter('email', 'password')(body)
        user = User(email=email)
        result = user.find_one(email=1, _id=1, hash=1)
        if result:
            is_valid = hash_generator.decode_hash(
                password=password, hash_storage=result['hash'])
            if is_valid:
                g.user_id = str(result['_id'])
            else:
                raise response_error.ResponseError(
                    code=401, message="The password is invalid")
        else:
            raise response_error.ResponseError(
                code=401, message="The user doesn't exist")
    except Exception as e:
        raise e


def verify_token():
    try:
        if 'HTTP_AUTHORIZATION' in request.headers.environ:
            authorization = request.headers.environ['HTTP_AUTHORIZATION']
            _, token = authorization.split(' ')
            decoded = token_generator.decode_token(token)
            user = User(id=decoded['user_id'])
            exist = user.count(_id=ObjectId(decoded['user_id']))
            if exist == 1:
                g.user_id = decoded['user_id']
            else:
                raise response_error.ResponseError(
                    code=403, message="You are not who you say you are")
        else:
            raise response_error.ResponseError(
                code=403, message="You are not who you say you are")
    except Exception as e:
        raise e
