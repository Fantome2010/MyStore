from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from .models import User
from datetime import timedelta
from django.utils.timezone import now
from .forms import EmailVerification


class UserRegistrationViewTestCase(TestCase):

    def setUp(self):
        self.path = reverse('users:registration')
        self.data = {
            'first_name': 'Den', 'last_name': 'Gord', 'username': 'Fant234', 'email': 'deng123@bk.ru',
            'password1': 'Rt@123dfgdf', 'password2': 'Rt@123dfgdf'
        }

    def test_user_registration_get(self):
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Store-Registration')
        self.assertTemplateUsed(response, 'users/registration.html')

    def test_user_registration_post_success(self):
        username = self.data['username']
        response = self.client.post(self.path, self.data)

        # check user registration
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('users:login'))
        self.assertTrue(User.objects.filter(username=username).exists())

        # check email verification
        email_verification = EmailVerification.objects.filter(user__username=username)
        self.assertTrue(email_verification.exists())
        self.assertEqual(
            email_verification.first().expiration.date(),
            (now() + timedelta(hours=48)).date()
        )

    def test_user_registration_post_error(self):
        username = self.data['username']
        User.objects.create(username=username)
        response = self.client.post(self.path, self.data)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, 'Пользователь с таким именем уже существует.', html=True)
