"""Users URLs."""

# Django
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')


urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html', redirect_authenticated_user=True), name='login'),

    path('logout/', LogoutView.as_view(next_page='loans:home'), name='logout'),

]
urlpatterns += router.urls
