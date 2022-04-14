from django import test as django_test
from django.contrib.auth import get_user_model
from django.urls import reverse

from bookstore_app.accounts.models import Profile

UserModel = get_user_model()


class ProfileDetailsViewTest(django_test.TestCase):
    VALID_USER_CREDENTIALS = {
        'username': 'testuser',
        'password': '12345',
    }

    VALID_PROFILE_DATA = {
        'first_name': 'Test',
        'last_name': 'User',
        'image_URL': 'http://test.picture/url.png',
        'gender': 'Male',
        'date_of_birth': '2020-09-29',
    }

    def test_when_all_valid__expect_correct_template(self):
        user = UserModel.objects.create_user(**self.VALID_USER_CREDENTIALS)
        profile = Profile.objects.create(
            **self.VALID_PROFILE_DATA,
            user=user,
        )

        response = self.client.get(reverse('profile details', kwargs={
            'pk': profile.pk,
        }))
        self.assertTemplateUsed('accounts/profile_details.html')


