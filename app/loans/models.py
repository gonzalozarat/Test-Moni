"""Loan Model"""
# Utils

import requests

# Django
from django.db import models
from django.conf import settings

# Utils
from utils.models import BaseModel

STATUS_WAITING = 0
STATUS_ACCEPTED = 1
STATUS_REJECTED = 2
STATUS_ERROR = 3

STATUS_CHOICES = (
    (STATUS_WAITING, 'En espera'),
    (STATUS_ACCEPTED, 'Aceptado'),
    (STATUS_REJECTED, 'Rechazado'),
    (STATUS_ERROR, 'Error'),
)


class Gender(BaseModel):
    """Gender Model"""

    name = models.CharField(max_length=20)
    slug_name = models.SlugField()

    def __str__(self):
        return self.slug_name


class Loan(models.Model):
    """Loan Model"""

    dni = models.IntegerField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    email = models.EmailField()
    monto = models.FloatField()
    status = models.IntegerField(
        choices=STATUS_CHOICES,
        default=STATUS_WAITING
    )

    def prescore(self):
        url = '{}{}'.format(settings.URL_LOAD, self.dni)
        header = {
            'credential': settings.CREDENTIAL
        }
        request = requests.get(url, headers=header)
        response = request.json()
        if response['has_error']:
            self.status = STATUS_ERROR
        elif response['status'] == 'approve':
            self.status = STATUS_ACCEPTED
        else:
            self.status = STATUS_REJECTED
        self.save()

    def get_status_name(self):
        return STATUS_CHOICES[self.status]
