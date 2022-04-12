from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.views import generic as views
from django.contrib.auth import views as auth_views, logout
from django.urls import reverse_lazy, reverse

from bookstore_app.accounts.forms import EditProfileForm, ProfileEditForm
from bookstore_app.accounts.models import Profile, BookstoreUser


class ProfileDetailsView(views.DetailView):
    model = Profile
    template_name = 'accounts/profile_details.html'
    context_object_name = 'profile'


class ProfileEditView(views.UpdateView):
    model = Profile
    form_class = EditProfileForm
    template_name = 'accounts/profile_edit.html'
    context_object_name = 'profile'

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse("profile details", kwargs={"pk": pk})

    def get_context_data(self, **kwargs):
        context = super(ProfileEditView, self).get_context_data(**kwargs)
        context['user_form'] = ProfileEditForm(instance=self.request.user)
        return context


def delete_profile(request, pk):
    user = BookstoreUser.objects.get(username=request.user.username)
    logout(request)
    user.delete()

    return redirect('success')


class Success(views.TemplateView):
    template_name = 'accounts/profile_delete_success.html'
