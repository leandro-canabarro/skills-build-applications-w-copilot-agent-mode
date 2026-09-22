from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class OctofitTrackerApiTests(APITestCase):
    def test_api_root_is_available(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Welcome to the OctoFit Tracker API', response.data.get('message', ''))

    def test_user_list_endpoint_returns_users(self):
        response = self.client.get(reverse('user-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_duplicate_user_email_is_rejected(self):
        User.objects.create_user(
            username='alex',
            email='alex@example.com',
            password='Password123!',
            first_name='Alex',
            last_name='Runner',
        )

        payload = {
            'username': 'newrunner',
            'email': 'alex@example.com',
            'password': 'Password123!',
            'first_name': 'New',
            'last_name': 'Runner',
            'display_name': 'New Runner',
            'fitness_level': 'beginner',
        }
        response = self.client.post(reverse('user-list'), payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)
