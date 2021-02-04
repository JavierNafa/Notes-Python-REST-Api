from __future__ import absolute_import
from app import app
from ast import literal_eval
from src.database.mongo import connect
from celery_config import configure_celery
from settings import flask_debug, flask_port

celery = configure_celery(app)
app.celery = celery

if __name__ == '__main__':
    with app.app_context():
        connect()
    app.run(host='0.0.0.0', port=flask_port, debug=literal_eval(flask_debug),
            use_reloader=False, threaded=True)
