from django.contrib.auth import get_user
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

class RegisterTest(TestCase):
    def test_user_registration(self):
        self.client.post(
            reverse('user:register'),

            data = {
                'username':'testadmin',
                'first_name':'bek',
                'last_name':'71x',
                'email':'bek@example.com',
                'password1':'somepassword',
                'password2':'somepassword',
            })

        user = User.objects.get(username='testadmin')

        self.assertEqual(user.first_name, 'bek')
        self.assertEqual(user.last_name, '71x')
        self.assertEqual(user.email, 'bek@example.com')
        self.assertNotEqual(user.password, 'somepassword')
        self.assertTrue(user.check_password('somepassword'))


    def test_registration_failed(self):
        response = self.client.post(
            reverse('user:register'),

            data = {
                'first_name':'testuser',
                'password':'<PASSWORD>',
            }
        )
        user_count = User.objects.count()

        self.assertEqual(user_count,0)
        self.assertFormError(response.context['form'], 'username', 'This field is required.')

    def test_invalid_email(self):
        response = self.client.post(
            reverse('user:register'),

            data = {
                'username':'testadmiin',
                'first_name':'test',
                'last_name':'user',
                'email':'email.com',
                'password1':'somepassword',
                'password2':'somepassword',
            })
        user_count = User.objects.count()
        self.assertEqual(user_count,0)
        self.assertFormError(response.context['form'], 'email', 'Enter a valid email address.')


class LoginTest(TestCase):
    def test_success_login(self):
        db_user = User.objects.create(username='testadmin', first_name='bek')
        db_user.set_password('somepassword')
        db_user.save()

        self.client.post(
            reverse('user:login'),

            data = {
                'username':'testadmin',
                'password':'somepassword'
            }
        )

        user= get_user(self.client)
        self.assertTrue(user.is_authenticated)

    def test_logget_out(self):
        def test_logged_out(self):
            db_user = User.objects.create(username='testadmin', first_name='bek')
            db_user.set_password('somepassword')
            db_user.save()
    
            self.client.post(
                reverse('user:login'),
                data={
                    'username': 'testadmin',
                    'password': 'somepassword'
                }
            )

            response = self.client.get(reverse('user:logout'))
            user = get_user(self.client)
            self.assertFalse(user.is_authenticated)