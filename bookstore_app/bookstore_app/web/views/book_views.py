from django.contrib.auth.decorators import login_required
from django.contrib.auth import mixins as auth_mixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic as views

from bookstore_app.web.forms import CreateBookForm, EditBookForm, CreateCommentForm, DeleteBookForm
from bookstore_app.web.models import Book, Comment


class BookCreateView(auth_mixin.LoginRequiredMixin, views.CreateView):
    template_name = 'book/book_create.html'
    form_class = CreateBookForm
    success_url = reverse_lazy('dashboard')


class BookEditView(auth_mixin.LoginRequiredMixin, views.UpdateView):
    model = Book
    form_class = EditBookForm
    template_name = 'book/book_edit.html'
    success_url = reverse_lazy('dashboard')
    context_object_name = 'book'


class BookDetailsView(views.DetailView):
    model = Book
    template_name = 'book/book_details.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        comments_connected = Comment.objects.filter(
            book=self.get_object()).order_by('-created_at')

        data['comments'] = comments_connected

        if self.request.user.is_authenticated:
            data['comment_form'] = CreateCommentForm(instance=self.request.user)

        return data

    def post(self, request, *args, **kwargs):
        new_comment = Comment(comment=request.POST.get('comment'),
                              user=self.request.user,
                              book=self.get_object())
        new_comment.save()
        return self.get(self, request, *args, **kwargs)


@login_required
def delete_book_view(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == "POST":
        form = DeleteBookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = DeleteBookForm(instance=book)

    context = {
        'form': form,
        'book': book,
    }
    return render(request, 'book/book_delete.html', context)
