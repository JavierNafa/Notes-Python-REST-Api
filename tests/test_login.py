from json import dumps
from tests.base_case import BaseCase


class TestLogin(BaseCase):
    def test_login_attempt(self):

        path = '/login/'
        email = 'example@example.com'
        password = '12345678'

        new_user = dumps({
            'name': 'example',
            'last_name': 'example',
            'email': email,
            'password': password
        })
        self.app.post('/user/',
                      headers={'Content-Type': 'application/json'},
                      data=new_user)

        success_response = self.app.post(path,
                                         headers={
                                             'Content-Type': 'application/json'},
                                         data=dumps({'email': email, 'password': password}))

        self.assertEqual(200, success_response.status_code,
                         success_response.json['message'])
        self.assertTrue(success_response.json['success'],
                        success_response.json['message'])

        fail_password_response = self.app.post(path,
                                               headers={
                                                   'Content-Type': 'application/json'},
                                               data=dumps({'email': email, 'password': '123456789'}))

        self.assertEqual(401, fail_password_response.status_code,
                         fail_password_response.json['message'])
        self.assertFalse(fail_password_response.json['success'],
                         fail_password_response.json['message'])

        fail_email_response = self.app.post(path,
                                            headers={
                                                'Content-Type': 'application/json'},
                                            data=dumps({'email': 'fail@fail.com', 'password': password}))

        self.assertEqual(401, fail_email_response.status_code,
                         fail_email_response.json['message'])
        self.assertFalse(fail_email_response.json['success'],
                         fail_email_response.json['message'])
