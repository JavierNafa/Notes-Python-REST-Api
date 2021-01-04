from os import getenv
from redis import Redis

host = getenv('REDIS_HOST') or '127.0.0.1'
port = getenv('REDIS_PORT') or 6379
db = getenv('REDIS_DB_INDEX') or 0

redis_conn = Redis(host=host, port=port, db=db)
