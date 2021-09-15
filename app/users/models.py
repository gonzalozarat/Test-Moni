""" User model."""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy

# Utilities
from utils.models import BaseModel


class User(BaseModel, AbstractUser):
    """ User model.Extend from Django's Abstract User, change the username field
    to email"""

    email = models.EmailField(
        'email',
        unique=True,
        error_messages={
            'unique': ugettext_lazy('Ya existe un usuario con este email')
        }
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.username
