import email
from rest_framework import status
from rest_framework.test import APITestCase, RequestsClient

from project.models import Project
from user.models import User

class ProjectTests(APITestCase):
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

    def test_user_login(self):
        url = ('http://127.0.0.1:8000/api/v1/users/users/')

        data = {
                "email": "john.doe@test.com",
                "username": "john.doe",
                "is_admin": True,
                "password": "10@testpass"
        }
        self.client.post(url, data, format='json')
        response = self.client.login(email='john.doe@test.com', password='10@testpass')
        self.assertTrue(response)
