import email
from rest_framework import status
from rest_framework.test import APITestCase, RequestsClient

from project.models import Project
from user.models import User

class ProjectTests(APITestCase):

    def setUp(self):

        # Ensure to hash the user password when creating a user
        user = User.objects.create(
            email="jane.doe@test.com",
            username= "jane.doe",
            is_active= True,
            is_admin=True,
        )
        user.set_password("10@testpass")
        user.save()

        # Generate token
        token_url ='http://127.0.0.1:8000/api/token/'
        data = {
            'email': 'jane.doe@test.com',
            'password': '10@testpass'
        }
        res = self.client.post(token_url, data, format='json')

        self.client.defaults['HTTP_AUTHORIZATION'] = 'Bearer ' + res.data['access'] 

    def test_user_is_active(self):
        user = User.objects.get(email='jane.doe@test.com')
        self.assertTrue(user.is_active)


    def test_create_project(self):
        """
        Ensure we can create a new project object
        """

        url = ('http://127.0.0.1:8000/api/v1/project/project/')
        data = {
                
                "name": "Project 2",
                "description": "Project 2 description",
                "release": [
                    {
                    "name": "Release 1",
                    "description": "Release 1 description "
                    },
                    {
                    "name": "Release 1",
                    "description": "Release 1 description "
                    },
                    {
                    "name": "Release 2",
                    "description": "Release 2 description "
                    },
                    {
                    "name": "Release 3",
                    "description": "Release 3 description "
                    }
                ]
                }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Project.objects.filter(name='Project 2').count(), 1)
        self.assertEqual(Project.objects.get().description, 'Project 2 description')

    def test_create_user(self):
        url = ('http://127.0.0.1:8000/api/v1/users/users/')

        data = {
                "email": "john.doe@test.com",
                "username": "john.doe",
                "is_admin": True,
                "password": "10@testpass"
            }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_create_super_user(self):
        url = ('http://127.0.0.1:8000/api/v1/users/users/')

        data = {
                "email": "john.doe@test.com",
                "username": "john.doe",
                "is_admin": True,
                "password": "10@testpass"
            }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_user_login(self):
        # create user
        user = User.objects.create(email='john.doe@test.com', username='john.doe', is_active=True)
        user.set_password('10@testpass')
        user.save()

        # login user
        response = self.client.login(email='john.doe@test.com', password='10@testpass')
        self.assertTrue(response)
