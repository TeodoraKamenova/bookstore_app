import datetime

from django.contrib.auth import models as auth_models
from django.core.validators import MinLengthValidator
from django.db import models

from bookstore_app.accounts.managers import BookstoreUserManager
from bookstore_app.common.validators import MinDateValidator, MaxDateValidator


class BookstoreUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    USERNAME_MAX_LENGTH = 25

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        unique=True,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'username'

    objects = BookstoreUserManager()


class Profile(models.Model):
    FIRST_NAME_MIN_LEN = 2
    FIRST_NAME_MAX_LEN = 15

    LAST_NAME_MIN_LEN = 2
    LAST_NAME_MAX_LEN = 15

    GENDER_MALE = 'Male'
    GENDER_FEMALE = 'Female'
    GENDER_OTHER = 'Other'
    GENDER_DO_NOT_SHOW = 'Do not show'

    GENDERS = (GENDER_MALE, GENDER_FEMALE, GENDER_OTHER, GENDER_DO_NOT_SHOW)

    GENDER_CHOICES = [(x, x) for x in GENDERS]

    MIN_DATE = datetime.date(1920, 1, 1)
    MAX_DATE = datetime.date(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day)

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LEN),
        ),
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LEN),
        ),

    )

    image_URL = models.URLField()

    gender = models.CharField(
        max_length=max(len(x) for x in GENDERS),
        choices=GENDER_CHOICES,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
        validators=(
            MinDateValidator(MIN_DATE),
            MaxDateValidator(MAX_DATE),
        )
    )

    user = models.OneToOneField(
        BookstoreUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def age(self):
        return datetime.datetime.now().year - self.date_of_birth.year
