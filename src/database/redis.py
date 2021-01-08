from redis import Redis
from settings import redis_db_index, redis_host, redis_port

host = redis_host or '127.0.0.1'
port = redis_port or 6379
db = redis_db_index or 0

redis_conn = Redis(host=host, port=port, db=db)
