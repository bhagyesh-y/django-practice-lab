from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class LoginViewTests(TestCase):
    def setUp(self):
        # Create a test user
        self.username = 'testuser'
        self.password = 'testpass123'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_login_with_valid_credentials(self):
        response = self.client.post(reverse('login'), {
            'username': self.username,
            'password': self.password
        })
        # After login, should redirect (status code 302)
        self.assertEqual(response.status_code, 302)

    def test_login_with_invalid_credentials(self):
        response = self.client.post(reverse('login'), {
            'username': self.username,
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Invalid credentials")

    def test_login_with_blank_fields(self):
        response = self.client.post(reverse('login'), {
            'username': '',
            'password': ''
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This field is required", html=False)

    def test_redirect_after_login(self):
        response = self.client.post(reverse('login'), {
            'username': self.username,
            'password': self.password
        })
        self.assertRedirects(response, reverse('home'))

    def test_logout(self):
        # Login first
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, reverse('login'))
