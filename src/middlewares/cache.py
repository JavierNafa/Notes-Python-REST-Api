from ast import literal_eval
from flask import request, g, make_response, jsonify
from src.repositories.redis_functions import get_key


def cache():
    try:
        if(request.method == 'GET'):
            blueprint = request.blueprint
            full_path = request.full_path
            key = f'{blueprint}_{full_path}'
            result = get_key(key)
            if(result):
                data = literal_eval((result.decode('utf-8')))
                return make_response(jsonify({'success': True, 'data': data, 'message': "OK"}), 200)
            g.key = key
    except Exception as e:
        raise e
