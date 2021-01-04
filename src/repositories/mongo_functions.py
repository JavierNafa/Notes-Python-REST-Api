from src.database.mongo import get_db


class MongoFunctions:

    def __init__(self, collection, **props):
        self.collection = collection
        self.__dict__.update(props)

    def __filter_props(self):
        filtered_properties = {key: value for (
            key, value) in self.__dict__.items() if value and key != 'collection'}.copy()
        return filtered_properties

    def __filter_params(self, **params):
        filtered_params = {key: value for (
            key, value) in params.items() if value}.copy()
        return filtered_params

    def insert(self):
        try:
            props = self.__filter_props()
            result = get_db()[self.collection].insert_one(props)
            return result
        except Exception as e:
            raise e

    def count(self, **filters):
        try:
            result = get_db()[self.collection].count_documents(filters)
            return result
        except Exception as e:
            raise e

    def find_one(self, **projection):
        try:
            props = self.__filter_props()
            result = get_db()[self.collection].find_one(
                props, projection=projection)
            return result
        except Exception as e:
            raise e

    def find(self, filters, projection, page=None, limit=None):
        try:
            params = self.__filter_params(**filters)
            result = get_db()[self.collection].find(
                params, projection=projection, skip=int(page) if page else 0, limit=int(limit) if limit else 10).sort('_id', -1)
            return list(result).copy()
        except Exception as e:
            raise e

    def update(self, search, **projection):
        try:
            props = self.__filter_props()
            result = get_db()[self.collection].find_one_and_update(
                search, {'$set': props}, projection=projection)
            return result
        except Exception as e:
            raise e

    def delete(self, **projection):
        try:
            props = self.__filter_props()
            result = get_db()[self.collection].find_one_and_delete(
                props, projection=projection)
            return result
        except Exception as e:
            raise e
