from datetime import datetime
from src.repositories.mongo_functions import MongoFunctions


class Note(MongoFunctions):

    def __init__(self, id=None, title=None, content=None, created=False, modified=False, user_id=None):
        self.collection = 'note'
        self._id = id
        self.title = title
        self.content = content
        self.creation_date = datetime.now().strftime(
            '%Y-%m-%d %H:%M:%S') if created else None
        self.modification_date = datetime.now().strftime(
            '%Y-%m-%d %H:%M:%S') if modified else None
        self.user_id = user_id
