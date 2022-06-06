from rest_framework import status
from rest_framework.test import APITestCase, RequestsClient

from project.models import Project

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