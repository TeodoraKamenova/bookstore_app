from django.contrib import admin

from bookstore_app.web.models import Author, Book, Comment


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]
