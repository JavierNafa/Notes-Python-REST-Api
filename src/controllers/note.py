from bson import ObjectId
from operator import itemgetter
from src.models.note import Note
from src.repositories.redis_functions import set_key


def post_note(**props):
    try:
        title, content, user_id = itemgetter(
            'title', 'content', 'user_id')(props)
        note = Note(title=title, content=content,
                    user_id=user_id, created=True, modified=True)
        is_duplicated = note.count(user_id=user_id, title=title)
        if is_duplicated >= 1:
            return {'success': False}
        result = note.insert()
        return {'success': True, 'data': {'title': title, 'content': content, '_id': str(result.inserted_id)}}
    except Exception as e:
        raise e


def get_note(filters):
    try:
        titles = filters.get('titles', None)
        from_date = filters.get('from_date', None)
        to_date = filters.get('to_date', None)
        page = filters.get('page', None)
        limit = filters.get('limit', None)
        user_id = filters.get('user_id')
        key = filters.get('key')
        note = Note(user_id=user_id)
        result = note.find({'user_id': user_id,
                            'title': {'$in': titles} if titles else None,
                            'creation_date': {'$gte': str(from_date), '$lte': str(to_date)} if from_date and to_date else None},
                           {'user_id': 0}, page=page, limit=limit)
        if len(list(result)) > 0:
            notes = list({**n, '_id': str(n['_id'])} for n in result)
            set_key(key, str(notes))
            return notes
        return []
    except Exception as e:
        raise e


def put_note(**props):
    try:
        id, user_id, title, content = itemgetter(
            'id', 'user_id', 'title', 'content')(props)
        object_id = ObjectId(id)
        note = Note(title=title, content=content, modified=True)
        is_duplicated = note.count(
            user_id=user_id, title=title, _id={'$ne': object_id})
        if is_duplicated >= 1:
            return {'success': False}
        result = note.update(
            {'user_id': user_id, '_id': object_id}, _id=0, title=1, content=1)
        return {'success': True, 'data': result}
    except Exception as e:
        raise e


def delete_note(**props):
    try:
        id, user_id = itemgetter(
            'id', 'user_id')(props)
        object_id = ObjectId(id)
        note = Note(id=object_id, user_id=user_id)
        result = note.delete(_id=0, title=1, content=1)
        return result
    except Exception as e:
        raise e
