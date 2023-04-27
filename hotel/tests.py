from django.test import TestCase
from . models import *
from .views import *
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import Client
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate

class SignUpPageTests(TestCase):
    def setUp(self) -> None:
        self.username = 'testuser'
        self.email = 'testuser@email.com'
        self.password = '@Khushab786'
        self.first_name = 'test'
        self.last_name = 'user'

    def test_signup_page_url(self):
        response = self.client.get("/register/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='register.html')

    def test_signup_page_view_name(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='register.html')

    def test_signup_form(self):
        response = self.client.post(reverse('register'), data={
            'username': self.username,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'password1': self.password,
            'password2': self.password
        })
        self.assertEqual(response.status_code, 302)