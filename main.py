from __future__ import absolute_import
from app import app
from src.database.mongo import connect
from celery_config import configure_celery

celery = configure_celery(app)
app.celery = celery

if __name__ == '__main__':
    with app.app_context():
        connect()
    app.run(port=8000, debug=True, use_reloader=False, threaded=True)
