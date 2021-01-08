from celery import Celery
from settings import broker, backend


celery = Celery('app', backend=backend,
                broker=broker)
