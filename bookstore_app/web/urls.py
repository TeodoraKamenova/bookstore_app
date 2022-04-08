from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from bookstore_app.web.views import BookCreateView, \
    BookEditView, AuthorDetailsView, CommentCreateView, BookDetailsView, DashboardView, HomeView, AuthorCreateView, \
    delete_book_view, AuthorEditView, delete_author_view

urlpatterns = [
                  path('', HomeView.as_view(), name='home page'),
                  path('dashboard/', DashboardView.as_view(), name='dashboard'),
                  path('book/add/', BookCreateView.as_view(), name='book add'),
                  path('book/edit<int:pk>/', BookEditView.as_view(), name='book edit'),
                  path('book/details<int:pk>/', BookDetailsView.as_view(), name='book details'),
                  path('book/delete<int:pk>/', delete_book_view, name='book delete'),
                  path('author/add/', AuthorCreateView.as_view(), name='author add'),
                  path('author/edit<int:pk>/', AuthorEditView.as_view(), name='author edit'),
                  path('author/details<int:pk>/', AuthorDetailsView.as_view(), name='author details'),
                  path('author/delete<int:pk>/', delete_author_view, name='author delete'),
                  path('comment/add<int:pk>', CommentCreateView.as_view(), name='comment add'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
