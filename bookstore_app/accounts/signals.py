from django.db.models import signals
from django.dispatch import receiver

from bookstore_app.accounts.models import Profile


# @receiver(signals.post_delete, sender=Profile)
# def delete_profile_books(sender, instance, *args, **kwargs):
#     try:
#         books = list(instance.book_set.all())
#         books.remove()
#     except:
#         pass