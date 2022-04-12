from django.contrib.auth.decorators import login_required
from django.contrib.auth import mixins as auth_mixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic as views

from bookstore_app.web.forms import EditCommentForm
from bookstore_app.web.models import Comment, Book


class CommentEditView(auth_mixin.LoginRequiredMixin, views.UpdateView):
    model = Comment
    form_class = EditCommentForm
    template_name = 'comment/comment_edit.html'

    def get_success_url(self):
        book = Book.objects.filter(comments=self.get_object())
        book_id = book.first().id
        return reverse_lazy('book details', kwargs={'pk': book_id})