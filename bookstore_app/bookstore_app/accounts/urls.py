from django.urls import path, reverse_lazy
from django.views.generic import RedirectView


from bookstore_app.accounts.views.profile_views import ProfileDetailsView, ProfileEditView, Success, \
    delete_profile
from bookstore_app.accounts.views.user_views import UserLoginView, \
    UserRegisterView, logout, change_password

urlpatterns = (
    path('register/', UserRegisterView.as_view(), name='register'),
    path('profile_details/<int:pk>/', ProfileDetailsView.as_view(), name='profile details'),
    path('profile/edit/<int:pk>/', ProfileEditView.as_view(), name='profile edit'),
    path('profile/delete/<int:pk>', delete_profile, name='profile delete'),
    path('profile/delete/success', Success.as_view(), name='success'),
    path('login/', UserLoginView.as_view(), name='login user'),
    path('logout/', logout, name='logout user'),
    path('password_change/', change_password, name='change password'),
    path('password_change_done/', RedirectView.as_view(url=reverse_lazy('dashboard')), name='password_change_done'),

)
