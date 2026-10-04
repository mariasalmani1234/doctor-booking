from rest_framework import serializers

from .models import Patient


class PatientSerializer(
    serializers.ModelSerializer
):

    userId = serializers.IntegerField(
        source='user.id',
        read_only=True
    )

    nationalCode = serializers.CharField(
        source='user.national_code',
        read_only=True
    )

    firstName = serializers.CharField(
        source='user.first_name',
        read_only=True
    )

    lastName = serializers.CharField(
        source='user.last_name',
        read_only=True
    )

    phone = serializers.CharField(
        source='user.phone',
        read_only=True
    )

    birthDate = serializers.DateField(
        source='birth_date',
        required=False,
        allow_null=True
    )

    class Meta:

        model = Patient

        fields = [
            'id',
            'userId',
            'nationalCode',
            'firstName',
            'lastName',
            'phone',
            'birthDate',
            'address',
        ]

        read_only_fields = [
            'id',
            'userId',
            'nationalCode',
            'firstName',
            'lastName',
            'phone',
        ]