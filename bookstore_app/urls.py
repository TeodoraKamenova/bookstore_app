from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('bookstore_app.accounts.urls')),
    path('', include('bookstore_app.web.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
