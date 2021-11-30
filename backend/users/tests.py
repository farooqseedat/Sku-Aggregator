from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
import json
from django.contrib.auth.hashers import make_password

import factory
from faker import Factory

from users.factory import UserFactory
from users.models import User

faker = Factory.create()

class UserTests(APITestCase):
    @classmethod
    def setUpClass (cls):
        super(UserTests, cls).setUpClass()
        cls.user_email = faker.email()
        cls.user_pass = faker.password()
        UserFactory(email=cls.user_email,
                    password=make_password(cls.user_pass),
                    admin=True, active=True, staff=True
                   )

    def setUp (self):
        self.client.login(email=self.user_email,password=self.user_pass)
        self.user_json = {
            "email": "fadad@fsf.com",
            "active": "True",
            "staff": "True",
            "first_name": "John",
            "last_name": "Doe",
            "admin": "True",
            "password": "123456fs",
            "profile":{
            "dob": "2015-06-05",
            "address": "Westwood colony",
            "country": "Nepal",
            "city": "Khatmandu",
            "zip": "56969"}
        }

    def test_user_list(self):
        url = reverse('user-list')
        UserFactory.create_batch(5)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']),6)

    def test_user_list_unauthorized(self):
        url = reverse('user-list')
        self.client.logout()
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_user(self):
        url = reverse('user-list')
        response = self.client.post(url, self.user_json, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_user(self):
        url = reverse('user-list')
        response = self.client.post(url, self.user_json, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.user_json["profile"]["address"] = "changed"
        url = reverse('user-detail', args=[response.data.get("id")])
        response = self.client.put(url, data=self.user_json, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["profile"]["address"],self.user_json["profile"]["address"])

    def test_delete_user_authorized(self):
        url = reverse('user-list')
        response = self.client.post(url, self.user_json, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        url = reverse('user-detail', args=[response.data.get("id")])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.count(),1)

    def test_delete_user_unauthorized(self):
        url = reverse('user-list')
        response = self.client.post(url, self.user_json, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        url = reverse('user-detail', args=[response.data.get("id")])
        self.client.logout()
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(User.objects.count(),2)

    def test_valid_login(self):
        url = '/users/login/'
        credentials = {"email": self.user_email, "password": self.user_pass}
        response = self.client.post(url, data=credentials, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_invalid_login(self):
        url = '/users/login/'
        credentials = {"email": self.user_email, "password": ""}
        response = self.client.post(url, data=credentials, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_refresh_access_token(self):
        url = '/users/login/'
        credentials = {"email": self.user_email, "password": self.user_pass}
        response = self.client.post(url, data=credentials, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        url = '/users/token-refresh/'
        refresh_token = response.data.get("refresh")
        response = self.client.post(url, data={"refresh": refresh_token}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.post(url, data={"refresh": ""}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
