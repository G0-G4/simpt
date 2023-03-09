from django.test import TestCase, Client
import json


# Create your tests here.

class ExampleTest(TestCase):
    def test(self):
        self.assertEqual(1, 1)

class RegisterTest(TestCase):
    def test_register(self):
        user = {
            "username": "user1",
            "email": "user1@mail.ru",
            "first_name": "first name",
            "last_name": "last name"
        }
        password = {
            "password": "user1user1",
            "password2": "user1user1",
        }
        c = Client()
        response = c.post('/users/register/', user | password)
        self.assertJSONEqual(json.dumps(user), json.dumps(response.json()))
