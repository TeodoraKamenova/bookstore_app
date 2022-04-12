from django.contrib.auth.decorators import login_required
from django.contrib.auth import mixins as auth_mixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic as views

from bookstore_app.web.forms import EditAuthorForm, DeleteBookForm, DeleteAuthorForm
from bookstore_app.web.models import Author


class AuthorCreateView(auth_mixin.LoginRequiredMixin, views.CreateView):
    model = Author
    fields = '__all__'
    template_name = 'author/author_create.html'
    success_url = reverse_lazy('author details')


class AuthorDetailsView(views.DetailView):
    model = Author
    template_name = 'author/author_details.html'
    context_object_name = 'author'


class AuthorEditView(auth_mixin.LoginRequiredMixin, views.UpdateView):
    model = Author
    form_class = EditAuthorForm
    template_name = 'author/author_edit.html'
    success_url = reverse_lazy('dashboard')
    context_object_name = 'author'


@login_required()
def delete_author_view(request, pk):
    author = Author.objects.get(pk=pk)
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
    return render(request, 'author/author_delete.html', context)

