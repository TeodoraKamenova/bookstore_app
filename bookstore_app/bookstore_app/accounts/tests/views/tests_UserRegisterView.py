from django import test as django_test
from django.contrib.auth import get_user_model
from django.urls import reverse

from bookstore_app.accounts.models import Profile

UserModel = get_user_model()


class UserRegisterViewTests(django_test.TestCase):
    VALID_PROFILE_DATA = {
        'username': 'Alex3',
        'password1': 'Dani2105!',
        'password2': 'Dani2105!',
        'first_name': 'Alex',
        'last_name': 'Kamenov',
        'image_URL': 'http://test.picture/url.png',
        'gender': 'Male',
        'date_of_birth': '2020-09-29',
    }

    def test_signup_page_url(self):
        response = self.client.get("/accounts/register/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='accounts/profile_create.html')

    def test_signup_page_view_name(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='accounts/profile_create.html')

    def test_create_profile__when_all_valid__expect_to_create(self):
        response = self.client.post(reverse('register'), data=self.VALID_PROFILE_DATA)
        self.assertEqual(response.status_code, 302)# redirect

        users = get_user_model().objects.all()
        self.assertEqual(users.count(), 1)

    def test_create_profile__when_all_valid__expect_to_redirect_to_details(self):
        response = self.client.post(
            reverse('register'),
            data=self.VALID_PROFILE_DATA,
        )

        expected_url = reverse('login user')
        self.assertRedirects(response, expected_url)