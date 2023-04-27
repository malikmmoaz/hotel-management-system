# from django.test import TestCase
# from .views import *
# fro

# # implement test case for register guest
# class RegisterGuestTestCase(TestCase):
#     def setUp(self):
#         self.data = {
#             'username': 'test',
#             'email': 'abc@gmail.com',
#             'password2': 'teststate',
#         }
    
#     def test_register_guest(self):
#         response = self.client.post('gregister/', self.data)
#         print('test: ' + str(response))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'register2.html')
#         self.assertContains(response, 'Guest registered successfully')

# # run test case
# # python manage.py test guest.tests.RegisterGuestTestCase