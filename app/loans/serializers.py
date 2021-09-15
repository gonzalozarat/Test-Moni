"""Loan serializer"""

# Django REST Framework
from rest_framework import serializers

# Models
from .models import Loan, Gender


class LoanSerializer(serializers.ModelSerializer):
    """Loan Model Serializer"""
    gender = serializers.SlugRelatedField(
        queryset=Gender.objects.all(),
        slug_field='slug_name')
    gender_name = serializers.SerializerMethodField()
    status_name = serializers.SerializerMethodField()

    class Meta:
        model = Loan
        fields = ('id', 'first_name', 'last_name', 'dni', 'gender', 'email',
                  'monto', 'status', 'gender_name', 'status_name')
        read_only_fields = ('status', 'gender_name', 'status_name')

    def get_gender_name(self, obj):
        return obj.gender.name

    def get_status_name(self, obj):
        return obj.get_status_name()

    def validate_dni(self, data):
        dni = data
        if len(str(dni)) < 7 or len(str(dni)) > 8:
            raise serializers.ValidationError('El DNI ingresado no es valido')
        return data

    def validate_monto(self, data):
        monto = data
        if monto < 1:
            raise serializers.ValidationError('El monto debe ser mayor a 0')
        return data

    def create(self, data):
        loan = Loan.objects.create(
            **data
        )
        loan.prescore()

        return loan


class GenderSerializer(serializers.ModelSerializer):

    """Gender Model Serializer"""

    class Meta:
        model = Gender
        fields = ('name', 'slug_name')
        lookup_field = 'slug_name'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
