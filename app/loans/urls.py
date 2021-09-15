# Django
from django.urls import path

# Rest
from rest_framework import routers

# ViewSets
from .views import LoanListViewSet, GenderViewSet, LoanViewSet
from . import views

# Router Rest
router = routers.SimpleRouter()
router.register(r'genders', GenderViewSet, basename='genders')
router.register('nuevo_prestamo', LoanViewSet, basename='nuevoPrestamo')
router.register('lista_prestamos', LoanListViewSet, basename='listaPrestamo')

urlpatterns = [
    path('new_loan/', views.nuevo_prestamo, name='new_loan'),
    path('list_loans/', views.lista_prestamos, name='list_loans'),
    path('home/', views.home, name='home'),
]
urlpatterns += router.urls
