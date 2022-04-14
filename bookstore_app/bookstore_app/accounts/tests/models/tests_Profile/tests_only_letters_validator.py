from django import test as django_test
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from bookstore_app.accounts.models import Profile

UserModel = get_user_model()


class ProfileFirstNameTest(django_test.TestCase):
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

    INVALID_PROFILE_DATA_CONTAINS_A_DIGIT = {
        'first_name': 'Test1',
        'last_name': 'User',
        'image_URL': 'http://test.picture/url.png',
        'gender': 'Male',
        'date_of_birth': '2020-09-29',
    }

    INVALID_PROFILE_DATA_CONTAINS_A_DOLLAR_SIGN = {
        'first_name': 'Te$st',
        'last_name': 'User',
        'image_URL': 'http://test.picture/url.png',
        'gender': 'Male',
        'date_of_birth': '2020-09-29',
    }

    INVALID_PROFILE_DATA_CONTAINS_A_SPACE = {
        'first_name': 'Te st',
        'last_name': 'User',
        'image_URL': 'http://test.picture/url.png',
        'gender': 'Male',
        'date_of_birth': '2020-09-29',
    }

    def test_profile_create__when_first_name_contains_only_letters__expect_success(self):
        user = UserModel.objects.create_user(**self.VALID_USER_CREDENTIALS)
        profile = Profile.objects.create(
            **self.VALID_PROFILE_DATA,
            user=user,
        )

        profile.save()
        self.assertIsNotNone(profile.pk)

    def test_profile_create__when_first_name_contains_a_digit__expect_to_fail(self):
        user = UserModel.objects.create_user(**self.VALID_USER_CREDENTIALS)
        profile = Profile.objects.create(
            **self.INVALID_PROFILE_DATA_CONTAINS_A_DIGIT,
            user=user,
        )

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)

    def test_profile_create__when_first_name_contains_a_dollar_sign__expect_to_fail(self):
        user = UserModel.objects.create_user(**self.VALID_USER_CREDENTIALS)
        profile = Profile.objects.create(
            **self.INVALID_PROFILE_DATA_CONTAINS_A_DOLLAR_SIGN,
            user=user,
        )

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)

    def test_profile_create__when_first_name_contains_a_space__expect_to_fail(self):
        user = UserModel.objects.create_user(**self.VALID_USER_CREDENTIALS)
        profile = Profile.objects.create(
            **self.INVALID_PROFILE_DATA_CONTAINS_A_SPACE,
            user=user,
        )

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()  # This is called in ModelForms implicitly
            profile.save()

        self.assertIsNotNone(context.exception)

    def test_profile_full_name__when_valid__expect_correct_full_name(self):
        profile = Profile(**self.VALID_PROFILE_DATA)

        expected_fullname = f'{self.VALID_PROFILE_DATA["first_name"]} {self.VALID_PROFILE_DATA["last_name"]}'
        self.assertEqual(expected_fullname, profile.full_name)