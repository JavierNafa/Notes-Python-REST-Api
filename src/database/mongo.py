from pymongo import MongoClient
from settings import mongo_db_name, mongo_host, mongo_port

host = mongo_host or '127.0.0.1'
port = mongo_port or 27017
db_name = mongo_db_name or 'notes'
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
