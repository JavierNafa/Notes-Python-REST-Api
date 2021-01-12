from json import dumps
from tests.base_case import BaseCase
from datetime import datetime, timedelta


class TestNote(BaseCase):

    path = '/note/'

    def __add_note(self):

        token = self.signup_and_login()

        payload = dumps({
            'title': 'test',
            'content': 'this is a content test'
        })

        success_response = self.app.post(self.path,
                                         headers={
                                             'Content-Type': 'application/json', 'Authorization': f'Bearer {token}'},
                                         data=payload)
        return token, success_response.json['data']

    def test_new_note(self):

        token = self.signup_and_login()

        payload = dumps({
            'title': 'test',
            'content': 'this is a content test'
        })

        success_response = self.app.post(self.path,
                                         headers={
                                             'Content-Type': 'application/json', 'Authorization': f'Bearer {token}'},
                                         data=payload)
        self.assertEqual(201, success_response.status_code,
                         success_response.json['message'])
        self.assertTrue(success_response.json['success'],
                        success_response.json['message'])

        fail_response = self.app.post(self.path,
                                      headers={
                                          'Content-Type': 'application/json', 'Authorization': f'Bearer {token}'},
                                      data=payload)
        self.assertEqual(400, fail_response.status_code,
                         fail_response.json['message'])
        self.assertFalse(fail_response.json['success'],
                         fail_response.json['message'])

    def test_find_note(self):

        token, data = self.__add_note()
        payload = {
            'from_date': (datetime.now() - timedelta(minutes=30)).strftime('%Y-%m-%d %H:%M:%S'),
            'to_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'titles': f"['{data['title']}']",
            'page': 0,
            'limit': 10
        }

        success_response = self.app.get(self.path,
                                        headers={
                                            'Authorization': f'Bearer {token}'},
                                        query_string=payload)
        self.assertEqual(200, success_response.status_code,
                         success_response.json['message'])
        self.assertTrue(success_response.json['success'],
                        success_response.json['message'])

        payload['to_date'] = None
        fail_response = self.app.get(self.path,
                                     headers={
                                         'Authorization': f'Bearer {token}'},
                                     query_string=payload)
        self.assertEqual(400, fail_response.status_code,
                         fail_response.json['message'])
        self.assertFalse(fail_response.json['success'],
                         fail_response.json['message'])

    def test_update_note(self):
        token, data = self.__add_note()
        note_id = data['_id']
        data.pop('_id', None)
        data['title'] = 'title updated'
        success_response = self.app.put(f'{self.path}{note_id}',
                                        headers={
                                            'Content-Type': 'application/json', 'Authorization': f'Bearer {token}'},
                                        data=dumps(data))
        self.assertEqual(200, success_response.status_code,
                         success_response.json['message'])
        self.assertTrue(success_response.json['success'],
                        success_response.json['message'])

        fail_response = self.app.put(f'{self.path}5fcad7e9b5f7221ea46561b6',
                                     headers={
                                         'Content-Type': 'application/json', 'Authorization': f'Bearer {token}'},
                                     data=dumps(data))
        self.assertEqual(400, fail_response.status_code,
                         fail_response.json['message'])
        self.assertFalse(fail_response.json['success'],
                         fail_response.json['message'])

    def test_delete_note(self):
        token, data = self.__add_note()
        note_id = data['_id']
        success_response = self.app.delete(f'{self.path}{note_id}',
                                           headers={
                                               'Authorization': f'Bearer {token}'})
        self.assertEqual(200, success_response.status_code,
                         success_response.json['message'])
        self.assertTrue(success_response.json['success'],
                        success_response.json['message'])

        fail_response = self.app.delete(f'{self.path}fail',
                                        headers={
                                            'Authorization': f'Bearer {token}'})

        self.assertEqual(400, fail_response.status_code,
                         fail_response.json['message'])
        self.assertFalse(fail_response.json['success'],
                         fail_response.json['message'])
