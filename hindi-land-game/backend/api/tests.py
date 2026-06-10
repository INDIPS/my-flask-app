"""
Tests for API views
"""
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from api.models import Player


class PlayerAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testplayer',
            email='test@example.com',
            password='testpass123'
        )
        self.player = Player.objects.create(
            user=self.user,
            character_type='student'
        )

    def test_get_player_stats(self):
        """Test retrieving player statistics"""
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/api/players/me/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['user']['username'], 'testplayer')

    def test_create_player_profile(self):
        """Test creating a new player profile"""
        user = User.objects.create_user(
            username='newplayer',
            email='new@example.com',
            password='newpass123'
        )
        self.client.force_authenticate(user=user)
        response = self.client.post('/api/players/create_profile/', {
            'character_type': 'farmer'
        })
        self.assertEqual(response.status_code, 201)
