from django import test as django_test
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from bookstore_app.accounts.models import Profile

UserModel = get_user_model()


class ProfileMinDateValidatorTest(django_test.TestCase):
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

    INVALID_PROFILE_DATA = {
        'first_name': 'Test',
        'last_name': 'User',
        'image_URL': 'http://test.picture/url.png',
        'gender': 'Male',
        'date_of_birth': '1919-09-29',
    }

    def test_when_correct_date__expect_success(self):
        user = UserModel.objects.create_user(**self.VALID_USER_CREDENTIALS)
        profile = Profile.objects.create(
            **self.VALID_PROFILE_DATA,
            user=user,
        )
        profile.save()
        self.assertIsNotNone(profile.pk)

    def test_when_earlier_than_expected_date_is_given__expect_to_raise(self):
        user = UserModel.objects.create_user(**self.VALID_USER_CREDENTIALS)
        profile = Profile.objects.create(
            **self.INVALID_PROFILE_DATA,
            user=user,
        )

        with self.assertRaises(ValidationError):
            profile.save()
            profile.full_clean()


class ProfileMaxDateValidatorTest(django_test.TestCase):
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

    INVALID_PROFILE_DATA = {
        'first_name': 'Test',
        'last_name': 'User',
        'image_URL': 'http://test.picture/url.png',
        'gender': 'Male',
        'date_of_birth': '2023-09-29',
    }

    def test_when_correct_date__expect_success(self):
        user = UserModel.objects.create_user(**self.VALID_USER_CREDENTIALS)
        profile = Profile.objects.create(
            **self.VALID_PROFILE_DATA,
            user=user,
        )
        profile.save()
        self.assertIsNotNone(profile.pk)

    def test_when_earlier_than_expected_date_is_given__expect_to_raise(self):
        user = UserModel.objects.create_user(**self.VALID_USER_CREDENTIALS)
        profile = Profile.objects.create(
            **self.INVALID_PROFILE_DATA,
            user=user,
        )
        with self.assertRaises(ValidationError):
            profile.save()
            profile.full_clean()



