from src.utils import response_error
from src.middlewares.cache import cache
from flask import Blueprint, request, jsonify, make_response, g
from src.controllers.note import post_note, get_note, put_note, delete_note


note_blueprint = Blueprint(
    'note', __name__, template_folder='routes', static_folder='routes')

note_blueprint.before_request(cache)


@note_blueprint.route('/', methods=['POST'], strict_slashes=False)
def post():
    try:
        user_id = g.user_id
        data = g.request.copy()
        result = post_note(**{'user_id': user_id, **data})
        if(result['success']):
            return make_response(jsonify({'success': True, 'data': result['data'], 'message': 'OK'}), 201)
        raise response_error.ResponseError(
            code=400, data=data, message=f'You have created this note before')
    except Exception as e:
        raise e


@note_blueprint.route('/', methods=['GET'], strict_slashes=False)
def get():
    try:
        user_id = g.user_id
        key = g.key
        data = g.request.copy()
        result = get_note({'user_id': user_id, 'key': key, **data})
        return make_response(jsonify({'success': True, 'data': result, 'message': 'OK'}), 200)
    except Exception as e:
        raise e


@note_blueprint.route('/<id>', methods=['PUT'], strict_slashes=False)
def put(id):
    try:
        user_id = g.user_id
        data = g.request.copy()
        result = put_note(**{'user_id': user_id, **data})
        if(result['success']):
            return make_response(jsonify({'success': True, 'data': result['data'], 'message': 'OK'}), 200)
        raise response_error.ResponseError(
            code=400, data=data, message='Check if the title is not duplicated in another note, if the note exist or if the note id is ok')
    except Exception as e:
        raise e


@note_blueprint.route('/<id>', methods=['DELETE'], strict_slashes=False)
def delete(id):
    try:
        user_id = g.user_id
        data = g.request.copy()
        result = delete_note(**{'user_id': user_id, **data})
        return make_response(jsonify({'success': True, 'data': result, 'message': 'OK'}), 200)
    except Exception as e:
        raise e
