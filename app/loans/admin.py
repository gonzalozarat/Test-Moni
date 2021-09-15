"""Admin Loan"""

# Django
from django.contrib import admin

# Models
from .models import Loan, Gender


class CustomLoanAdmin(admin.ModelAdmin):
    """Loan model admin."""
    list_display = ('first_name', 'last_name', 'monto', 'email', 'status')


class CustomGenderAdmin(admin.ModelAdmin):
    """Gender model admin."""
    list_display = ('name', 'slug_name')


admin.site.register(Loan, CustomLoanAdmin)
admin.site.register(Gender, CustomGenderAdmin)
