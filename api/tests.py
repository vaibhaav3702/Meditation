from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import MeditationSession, ActivityLog

class MeditationMindingsTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.session = MeditationSession.objects.create(title='Morning Calm', description='A calm start.', duration_minutes=10)

    def test_create_user(self):
        data = {'username': 'newuser', 'password': 'newpassword', 'email': 'new@example.com'}
        response = self.client.post('/api/users/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_session(self):
        data = {'title': 'Evening Relax', 'description': 'Relax before bed.', 'duration_minutes': 15}
        response = self.client.post('/api/sessions/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_activity_log(self):
        data = {'user': self.user.id, 'session': self.session.id, 'notes': 'Felt great.'}
        response = self.client.post('/api/activity-logs/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_invalid_duration(self):
        data = {'title': 'Bad Session', 'description': 'Invalid duration.', 'duration_minutes': -5}
        response = self.client.post('/api/sessions/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
