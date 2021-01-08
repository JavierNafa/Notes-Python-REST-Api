from celery import Celery
from celery_holder import celery


def configure_celery(app):
    Task = celery.Task

    class ContextTask(Task):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return Task.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery
