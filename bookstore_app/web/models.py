from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models
from django.http import request

from bookstore_app.accounts.models import BookstoreUser


class Author(models.Model):
    FIRST_NAME_MIN_LEN = 2
    FIRST_NAME_MAX_LEN = 15

    LAST_NAME_MIN_LEN = 2
    LAST_NAME_MAX_LEN = 15

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

    image_url = models.URLField()

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name


class Book(models.Model):
    TITLE_MAX_LEN = 30

    CATEGORY_BIOGRAPHIES = 'Biographies'
    CATEGORY_CLASSICS = 'Classics'
    CATEGORY_COMICS = 'Comics'
    CATEGORY_COOKBOOKS = 'Cookbooks'
    CATEGORY_DETECTIVE_MYSTERY = 'Detective and Mystery'
    CATEGORY_FANTASY = 'Fantasy'
    CATEGORY_HISTORY = 'History'
    CATEGORY_HORROR = 'Horror'
    CATEGORY_POETRY = 'Poetry'
    CATEGORY_ROMANCE = 'Romance'
    CATEGORY_SCIENCE_FICTION = 'Science Fiction'

    CATEGORY_CHOICES = [
        (CATEGORY_BIOGRAPHIES, 'Biographies'),
        (CATEGORY_CLASSICS, 'Classics'),
        (CATEGORY_COMICS, 'Comics'),
        (CATEGORY_COOKBOOKS, 'Cookbooks'),
        (CATEGORY_DETECTIVE_MYSTERY, 'Detective and Mystery'),
        (CATEGORY_FANTASY, 'Fantasy'),
        (CATEGORY_HISTORY, 'History'),
        (CATEGORY_HORROR, 'Horror'),
        (CATEGORY_POETRY, 'Poetry'),
        (CATEGORY_ROMANCE, 'Romance'),
        (CATEGORY_SCIENCE_FICTION, 'Science Fiction'),
    ]

    title = models.CharField(
        max_length=TITLE_MAX_LEN,
    )

    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    image_URL = models.URLField()

    category = models.CharField(
        max_length=max(len(x) for x, _ in CATEGORY_CHOICES),
        choices=CATEGORY_CHOICES,
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Comment(models.Model):

    book = models.ForeignKey(
        'Book',
        on_delete=models.CASCADE,
        related_name='comments',
    )

    comment = models.TextField()

    created_at = models.DateField(
        auto_now_add=True
    )

    user = models.ForeignKey(
        BookstoreUser,
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f"Comment by {self.user} on {self.created_at}"