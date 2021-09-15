"""URL Configuration """

# Django
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path('', include(('loans.urls', 'loans'), namespace='loans')),
    path('', include(('users.urls', 'users'), namespace='users')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
