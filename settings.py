from os import getenv
from dotenv import load_dotenv

load_dotenv()


email_service = getenv('EMAIL_SERVICE')
email_port = getenv('EMAIL_PORT')
from_email = getenv('EMAIL_USER')
email_password = getenv('EMAIL_PASSWORD')
backend = getenv('CELERY_RESULT_BACKEND')
broker = getenv('CELERY_BROKER_URL')
flask_env = getenv('ENV')
secret_key = getenv('TOKEN_KEY')
redis_host = getenv('REDIS_HOST')
redis_port = getenv('REDIS_PORT')
redis_db_index = getenv('REDIS_DB_INDEX')
redis_expiration = getenv('REDIS_EXPIRATION')
mongo_host = getenv('MONGO_HOST')
mongo_port = getenv('MONGO_PORT')
mongo_db_name = getenv('MONGO_DB_NAME')
