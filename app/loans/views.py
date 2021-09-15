"""Loan views."""

# Django Rest Framework
from rest_framework import viewsets, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Permissions
from rest_framework.permissions import IsAuthenticated, AllowAny

# Models
from .models import Loan, Gender

# Serializers
from .serializers import LoanSerializer, GenderSerializer

# Django
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def lista_prestamos(request):
    return render(request, 'loans/list_loans.html')


def nuevo_prestamo(request):
    return render(request, 'loans/new_loans.html')


def home(request):
    return render(request, 'home.html')


class LoanListViewSet(viewsets.ModelViewSet):
    """Loan List view set"""
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    search_fields = ('dni', 'first_name', 'last_name', 'email')
    filterset_fields = ('status', 'gender')

    def get_permissions(self):
        permissions = []
        if self.action in ['update', 'partial_update', 'list', 'delete']:
            permissions.append(IsAuthenticated)
        if self.action == 'create':
            permissions.append(AllowAny)
        else:
            permissions.append(IsAuthenticated)
        return [permission() for permission in permissions]


class GenderViewSet(mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """Gender view set"""
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer

    def get_permissions(self):
        permissions = [AllowAny]
        return [permission() for permission in permissions]


class LoanViewSet(viewsets.ModelViewSet):
    """Loan view set"""
    serializer_class = LoanSerializer
    queryset = Loan.objects.all()
