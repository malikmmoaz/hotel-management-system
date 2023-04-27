from django.test import TestCase
from . models import *
from .views import *
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import Client
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
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

class loginTests (TestCase):
    def setUp(self) -> None:
        self.username = 'testuser'
        self.password = '@Khushab786'

    def test_login_page_url(self):
        response = self.client.get("/login/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='login.html')

    def test_login_page_view_name(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='login.html')

    def test_login_form(self):
        response = self.client.post(reverse('login'), data={
            'username': self.username,
            'password': self.password
        })
        self.assertEqual(response.status_code, 200)

class logoutTests (TestCase):
    def test_logout_page_url(self):
        response = self.client.get("/logout/")
        self.assertEqual(response.status_code, 302)

class changePwTest(TestCase):
    def setUp(self) -> None:
        self.username = 'testuser'
        self.email = 'testuser@email.com'
        self.password = '@Khushab786'
        self.new_pass = '@Khushab123'
        self.first_name = 'test'
        self.last_name = 'user'

    def test_change_password_form(self):
        # create user object and hotel manager object
        user = User.objects.create_user(username=self.username, email=self.email, password=self.password, first_name=self.first_name, last_name=self.last_name)
        hotel_manager = HotelManager.objects.create(user=user)
        # login user
        self.client.login(username=self.username, password=self.password)
        response = self.client.post(reverse('change_password'), data={
            'old_password': self.username,
            'new_password1': self.new_pass,
            'new_password2': self.new_pass
        })
        self.assertEqual(response.status_code, 200)

# class change_passwordTests (TestCase):
#     def setUp(self) -> None:
#         self.username = 'testuser'
#         self.password = '@Khushab786'
#         self.new_password = '@Khushab786'

#     def test_change_password_page_url(self):
#         response = self.client.get("/change_password/")
#         self.assertEqual(response.status_code, 302)
#         self.assertTemplateUsed(response, template_name='change_password.html')

#     def test_change_password_page_view_name(self):
#         response = self.client.get(reverse('change_password'))
#         self.assertEqual(response.status_code, 302)
#         self.assertTemplateUsed(response, template_name='change_password.html')

#     def test_change_password_form(self):
#         response = self.client.post(reverse('change_password'), data={
#             'username': self.username,
#             'password': self.password,
#             'new_password': self.new_password
#         })
#         self.assertEqual(response.status_code, 302)

# class hotel_applicationTests(TestCase):
#     def setUp(self) -> None:
#         self.hotel_name = 'testhotel'
#         self.hotel_address = 'testaddress'
#         self.hotel_contact = '1234567890'
#         self.hotel_email = 'testhotel@email.com'
#         self.hotel_description = 'testdescription'
#         self.latitude = '1234567890'
#         self.longitude = '1234567890'

#     def test_hotel_application_page_url(self):
#         response = self.client.get("/hotel_application/")
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, template_name='hotel_application.html')

#     def test_hotel_application_page_view_name(self):
#         response = self.client.get(reverse('hotel_application'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, template_name='hotel_application.html')

#     def test_hotel_application_form(self):
#         response = self.client.post(reverse('hotel_application'), data={
#             'hotel_name': self.hotel_name,
#             'hotel_address': self.hotel_address,
#             'hotel_contact': self.hotel_contact,
#             'hotel_email': self.hotel_email,
#             'hotel_description': self.hotel_description,
#             'latitude': self.latitude,
#             'longitude': self.longitude
#         })
#         self.assertEqual(response.status_code, 302)


# class change_hoteldetailsTests (TestCase):
#     def setUp(self) -> None:
#         self.hotel_name = 'testhotel'
#         self.hotel_address = 'testaddress'
#         self.hotel_contact = '1234567890'
#         self.hotel_email = 'testhotel@email.com'
#         self.hotel_description = 'testdescription'
#         self.latitude = '1234567890'
#         self.longitude = '1234567890'

#     def test_change_hoteldetails_page_url(self):
#         response = self.client.get("/change_hoteldetails/") #change the url here according to the updated url
#         self.assertEqual(response.status_code, 302)
#         self.assertTemplateUsed(response, template_name='change_hoteldetails.html')

#     def test_change_hoteldetails_page_view_name(self):
#         response = self.client.get(reverse('change_hoteldetails'))
#         self.assertEqual(response.status_code, 302)
#         self.assertTemplateUsed(response, template_name='change_hoteldetails.html')

#     def test_change_hoteldetails_form(self):
#         response = self.client.post(reverse('change_hoteldetails'), data={
#             'hotel_name': self.hotel_name,
#             'hotel_address': self.hotel_address,
#             'hotel_contact': self.hotel_contact,
#             'hotel_email': self.hotel_email,
#             'hotel_description': self.hotel_description,
#             'latitude': self.latitude,
#             'longitude': self.longitude
#         })
#         self.assertEqual(response.status_code, 302)


    


