from os import getenv
from src.database.redis import redis_conn

expiration = getenv('REDIS_EXPIRATION') or 60


def set_key(key, data: str, ex=expiration):
    try:
        result = redis_conn.set(key, data, ex=int(ex))
        return result
    except Exception as e:
        raise e


def get_key(key):
    try:
        result = redis_conn.get(key)
        return result
    except Exception as e:
        raise e
