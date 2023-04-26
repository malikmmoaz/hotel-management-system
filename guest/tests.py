from django.test import TestCase
from .views import *

# implement test case for register guest
class RegisterGuestTestCase(TestCase):
    def setUp(self):
        self.data = {
            'username': 'test',
            'email': 'abc@gmail.com',
            'first_name': '1234567890',
            'last_name': 'test address',
            'password1': 'test city',
            'password2': 'test state',
        }
    
    def test_register_guest(self):
        response = self.client.post('gregister/', self.data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'guest/register.html')
        self.assertContains(response, 'Guest registered successfully')

# run test case
# python manage.py test guest.tests.RegisterGuestTestCase