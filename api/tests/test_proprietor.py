from django.test import TestCase, Client
from rest_framework import reverse
from django.contrib.auth import get_user_model


CREATE_URL = reverse('api:create_proprietor')
class TestProprietorModel(TestCase):
    def setUp(self):
        self.client = Client()
        password = 'abvcdd'
        self.user = get_user_model().objects.create_user(
            email='test@test.com',
            password=password
        )

    def test_liscence_no_complete(self):
        data = {
            'name':'akpan',
            'age': '15',
            'sex': 'male',
            'city': 'awka',
            'user': self.user,
            'car_model': 'hyundai',
            'liscence_no': '124'
        }
        res = self.client.post(data, CREATE_URL)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
