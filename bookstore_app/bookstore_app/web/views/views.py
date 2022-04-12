from django.views import generic as views

from bookstore_app.common.mixins import RedirectToDashboard
from bookstore_app.web.models import Book


class HomeView(RedirectToDashboard, views.TemplateView):
    template_name = 'home_page.html'


class DashboardView(views.ListView):
    model = Book
    template_name = 'dashboard.html'
    paginate_by = 6
    ordering = ('title',)
    context_object_name = 'books'

