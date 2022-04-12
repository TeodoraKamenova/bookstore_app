from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('bookstore_app.accounts.urls')),
    path('', include('bookstore_app.web.urls')),
]
