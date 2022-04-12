from django.urls import path

from bookstore_app.web.views.author_views import AuthorCreateView, AuthorEditView, AuthorDetailsView, delete_author_view
from bookstore_app.web.views.book_views import BookCreateView, BookEditView, BookDetailsView, delete_book_view
from bookstore_app.web.views.comment_views import CommentEditView
from bookstore_app.web.views.views import HomeView, DashboardView

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
                  path('comment/edit<int:pk>/', CommentEditView.as_view(), name='comment edit'),
              ]
