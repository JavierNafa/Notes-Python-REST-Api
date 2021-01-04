from jwt import InvalidTokenError
from pymongo.errors import PyMongoError
from marshmallow import ValidationError
from flask import jsonify, make_response
from src.utils.response_error import ResponseError


def handle_errors(error):
    code = getattr(error, 'code', 500)
    if isinstance(error, ValidationError):
        return make_response(jsonify({'success': False, 'data': error.messages, 'message': "Invalid value, pls don't try to hack this"}), 400)
    if isinstance(error, InvalidTokenError):
        return make_response(jsonify({'success': False, 'data': None, 'message': 'You are not who you say you are'}), 403)
    if isinstance(error, ModuleNotFoundError):
        return make_response(jsonify({'success': False, 'data': None, 'message': "This route doesn't exist"}), 404)
    if isinstance(error, ResponseError):
        return make_response(jsonify({'success': False, 'data': error.data, 'message': error.message}), error.status)
    if isinstance(error, PyMongoError):
        return make_response(jsonify({'success': False, 'data': None, 'message': 'You killed the DB'}), 500)
    return make_response(jsonify({'success': False, 'data': None, 'message': f'This should not happen: {error}'}), code)
