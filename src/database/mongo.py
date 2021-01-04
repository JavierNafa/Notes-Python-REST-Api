import os
from pymongo import MongoClient

host = os.getenv('MONGO_HOST')
port = os.getenv('MONGO_PORT') or '27017'
db_name = os.getenv('MONGO_DB_NAME') or 'notes'
db = None
client = None


def connect():
    global db, client
    client = MongoClient(host, int(port))
    db = client.get_database(db_name)
    db.user.create_index('email')
    db.note.create_index('title')
    db.note.create_index('creationDate')
    db.note.create_index('userId')
    print('Connected to mongo')


def get_db():
    return db
