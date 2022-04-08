from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic as views

from bookstore_app.common.mixins import RedirectToDashboard
from bookstore_app.web.forms import EditBookForm, CreateCommentForm, CreateBookForm, DeleteBookForm, EditAuthorForm, \
    DeleteAuthorForm
from bookstore_app.web.models import Book, Author, Comment


class HomeView(RedirectToDashboard, views.TemplateView):
    template_name = 'home_page.html'


class DashboardView(views.ListView):
    model = Book
    template_name = 'dashboard.html'
    paginate_by = 6
    ordering = ('title',)
    context_object_name = 'books'


class BookCreateView(LoginRequiredMixin, views.CreateView):
    template_name = 'book_create.html'
    form_class = CreateBookForm
    success_url = reverse_lazy('dashboard')

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs['user'] = self.request.user
    #     return kwargs


class BookEditView(LoginRequiredMixin, views.UpdateView):
    model = Book
    form_class = EditBookForm
    template_name = 'book_edit.html'
    success_url = reverse_lazy('dashboard')
    context_object_name = 'book'


class BookDetailsView(LoginRequiredMixin, views.DetailView):
    model = Book
    template_name = 'book_details.html'
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
    return render(request, 'book_delete.html', context)


class AuthorCreateView(LoginRequiredMixin, views.CreateView):
    model = Author
    fields = '__all__'
    template_name = 'author_create.html'
    success_url = reverse_lazy('author details')


class AuthorDetailsView(LoginRequiredMixin, views.DetailView):
    model = Author
    template_name = 'author_details.html'
    context_object_name = 'author'


class AuthorEditView(views.UpdateView):
    model = Author
    form_class = EditAuthorForm
    template_name = 'author_edit.html'
    success_url = reverse_lazy('dashboard')
    context_object_name = 'author'


def delete_author_view(request, pk):
    author= Author.objects.get(pk=pk)
    if request.method == "POST":
        form = DeleteBookForm(request.POST, request.FILES, instance=author)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = DeleteAuthorForm(instance=author)

    context = {
        'form': form,
        'author': author,
    }
    return render(request, 'author_delete.html', context)


class CommentCreateView(views.CreateView):
    form_class = CreateCommentForm
    template_name = 'comment-create.html'
    success_url = reverse_lazy('book details')

