from flask import Blueprint, request, jsonify, make_response, g
from src.controllers.user import post_user
from src.utils.response_error import ResponseError

user_blueprint = Blueprint(
    'user', __name__, template_folder='routes', static_folder='routes')


@user_blueprint.route('/', methods=['POST'], strict_slashes=False)
def post():
    try:
        data = g.request.copy()
        result = post_user(**data)
        if(result['success']):
            return make_response(jsonify({'success': True, 'data': result['data'], 'message': 'OK'}), 201)
        raise ResponseError(
            code=400, data=data, message='Email already exist, are you trying to hack someone?')
    except Exception as e:
        raise e
