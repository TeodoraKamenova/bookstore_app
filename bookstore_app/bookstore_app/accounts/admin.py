from django.contrib import admin

from bookstore_app.accounts.models import BookstoreUser


@admin.register(BookstoreUser)
class BookstoreUserAdmin(admin.ModelAdmin):

    def group(self, user):
        groups = []
        for group in user.groups.all():
            groups.append(group.name)
        return ' '.join(groups)

    group.short_description = 'Groups'

    list_display = ('username', 'is_superuser', 'is_staff','group', )
