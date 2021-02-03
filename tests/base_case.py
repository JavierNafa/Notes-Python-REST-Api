from main import app
from json import dumps
from unittest import TestCase
from src.database import mongo
from src.database import redis


class BaseCase(TestCase):
    def setUp(self):
        self.app = app.test_client()
        mongo.connect()

    def tearDown(self):
        redis.redis_conn.flushall()
        mongo.get_client().close()
        mongo.get_client().drop_database('notes')
        redis.redis_conn.close()

    def signup_and_login(self):
        email = 'example@example.com'
        password = '12345678'
        payload = dumps({
            'name': 'example',
            'last_name': 'example',
            'email': email,
            'password': password
        })
        self.app.post(
            '/user/', headers={'Content-Type': 'application/json'}, data=payload)
        response = self.app.post(
            '/login/', headers={'Content-Type': 'application/json'}, data=dumps({'email': email, 'password': password}))
        return response.json['data']
