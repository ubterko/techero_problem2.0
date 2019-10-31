from rest_framework import status
from rest_framework.test import APIClient
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


class PatronTests(TestCase):

    """contains various tests for Patron api"""
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            email='testuser@gmail.com',
            password='testpass123'
    )

    def test_patron_create(self):
      data = {'user':self.user,
              'name':'Ada',
              'age':'23',
              'sex':'Female',
              'city':'Port Harcourt',
        }

      url = reverse('api:create_patron')
      res = self.client.post(url, data)

      self.assertEqual(res.status_code, status.HTTP_200_OK)
