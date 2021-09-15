"""Loans tests."""

# Django
from django.test import TestCase
from django.urls import reverse

# Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase

# Model
from .models import Loan, Gender
from users.models import User


class LoansTestCase(TestCase):
    """Loans test case."""
    fixtures = ["genders.json"]

    def setUp(self):
        self.loan = Loan.objects.create(
            first_name="Gonzalo",
            last_name="Zarate",
            dni=41265121,
            gender=Gender.objects.get(slug_name="M"),
            email="gonzalozarate988@gmail.com",
            monto=30000,
        )

    def test_prescore(self):
        self.loan.prescore()
        self.assertGreater(self.loan.status, 0)


class LoansAPITestCase(APITestCase):
    """Loans API test case."""
    fixtures = ["genders.json"]

    def setUp(self):
        self.user = User.objects.create(
            first_name='Alejandro',
            last_name='Zarate',
            email='alejandro2020@gmail.com',
            username='alejandro2020@gmail.com',
            password='123456'
        )

        self.loan = Loan.objects.create(
            first_name="Liliana",
            last_name="Pereyra",
            dni=21901416,
            gender=Gender.objects.get(slug_name="F"),
            email="liliana_flor33@hotmail.com",
            monto=20000,
        )

        # URLs
        self.url = reverse('loans:nuevoPrestamo-list')
        self.url_detail = reverse('loans:listaPrestamo-detail', kwargs={'pk': self.loan.id})

    def test_response_success(self):
        """Verify request succeed."""
        request = self.client.get(self.url)
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_loan_creation(self):
        """Verify loans are generated if none exist previously."""
        # Loans in DB must be 1
        self.assertEqual(Loan.objects.count(), 1)

        # Call loan create URL
        request = self.client.post(self.url, data={
            "first_name": "Gaston",
            "last_name": "Zarate",
            "dni": 38001975,
            "gender": "M",
            "email": "gaston.z195@gmail.com",
            "monto": 40000
        })
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)

        # Loans in DB must be 2
        self.assertEqual(Loan.objects.count(), 2)

    def test_loan_delete(self):
        """Verify loans are deleted."""
        count_loans = Loan.objects.count()
        request = self.client.delete(self.url_detail)
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(count_loans-1, Loan.objects.count())
