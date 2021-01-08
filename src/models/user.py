from src.repositories.mongo_functions import MongoFunctions


class User(MongoFunctions):

    def __init__(self, id=None, name=None, last_name=None, email=None, hash=None):
        self.collection = 'user'
        self._id = id
        self.name = name
        self.last_name = last_name
        self.email = email
        self.hash = hash
