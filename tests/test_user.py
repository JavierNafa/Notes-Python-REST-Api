from json import dumps
from tests.base_case import BaseCase


class TestUser(BaseCase):

    def test_new_user(self):
        path = '/user/'
        payload = dumps({
            'name': 'example',
            'last_name': 'example',
            'email': 'example@example.com',
            'password': '12345678'
        })
        success_response = self.app.post(path,
                                         headers={
                                             'Content-Type': 'application/json'},
                                         data=payload)
        self.assertEqual(201, success_response.status_code,
                         success_response.json['message'])
        self.assertTrue(success_response.json['success'],
                        success_response.json['message'])

        fail_response = self.app.post(path,
                                      headers={
                                          'Content-Type': 'application/json'},
                                      data=payload)
        self.assertEqual(400, fail_response.status_code,
                         fail_response.json['message'])
        self.assertFalse(fail_response.json['success'],
                         fail_response.json['message'])
