from flask import request, g
from importlib import import_module


def validate():
    try:
        method = request.method.upper()
        _, route, *tail = request.path.split('/')
        schema = import_module(f'src.schemas.{route}')
        body = request.json or {}
        query = request.args or {}
        params = request.view_args or {}
        properties = {**body, **query, **params}
        result = getattr(schema, f'{method}')().load(properties)
        g.request = result.copy()
    except Exception as e:
        raise e
