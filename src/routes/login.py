from src.controllers.login import post_login
from flask import Blueprint, request, jsonify, make_response, g


login_blueprint = Blueprint(
    'login', __name__, template_folder='routes', static_folder='routes')


@login_blueprint.route('/', methods=['POST'], strict_slashes=False)
def post():
    try:
        user_id = g.user_id
        token = post_login(user_id)
        return make_response(jsonify({'success': True, 'data': token, 'message': 'OK'}), 200)
    except Exception as e:
        raise e
