from app import app
from src.database.mongo import connect

if __name__ == '__main__':
    with app.app_context():
        connect()
    app.run(port=8000, debug=True, use_reloader=False, threaded=True)
