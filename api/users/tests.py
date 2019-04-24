from rest_framework.test import APITestCase
from rest_framework import status
from .models import User


class UserTest(APITestCase):
    def test_create_user(self):
        self.assertEquals(User.objects.all().count(), 0)
        test_case = [
            {
                "username": "flatcoke",
                "email": "flatcoke89@a.com",
                "password": "qwer1234"
            }
        ]
        for i in test_case:
            res = self.client.post('/api/v1/users/', data=i)
            self.assertEquals(res.status_code, status.HTTP_201_CREATED)
        self.assertEquals(len(test_case), User.objects.all().count())

    def test_create_user_not_found_password(self):
        self.assertEquals(User.objects.all().count(), 0)
        test_case = [
            {
                "username": "flatcoke",
                "email": "flatcoke89@a.com",
            }, {
                "username": "flatcoke",
                'password': 'password',
            }, {
                "email": "flatcoke89@a.com",
                'password': 'password',
            },
        ]
        for i in test_case:
            res = self.client.post('/api/v1/users/', data=i)
            self.assertEquals(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEquals(0, User.objects.all().count())

    def test_create_user_hash_password(self):
        self.assertEquals(User.objects.all().count(), 0)
        data = {
            "username": "flatcoke",
            "email": "flatcoke89@a.com",
            "password": "qwer1234"
        }
        res = self.client.post('/api/v1/users/', data=data)
        self.assertEquals(res.status_code, status.HTTP_201_CREATED)

        self.assertNotEqual(User.objects.first().password, data['password'])

    def get_token(self):
        res = self.client.post('/api/auth/token')
        return res.data.get('token')

    def test_generate_token(self):
        token = self.get_token()
        self.assertIsNotNone(token)

    def test_get_user_without_token(self):
        res = self.client.post('/api/v1/users/1/')
        self.assertEquals(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_user_with_token(self):
        res = self.client.post('/api/auth/token/')
        self.assertEquals(res.status_code, status.HTTP_201_CREATED)
        token = res.data['token']

        headers = {
            'authorize': token
        }

        res = self.client.post('/api/v1/users/1/', **headers)
        self.assertEquals(res.status_code, status.HTTP_200_OK)
