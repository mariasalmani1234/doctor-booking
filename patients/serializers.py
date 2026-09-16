from rest_framework import serializers

from .models import Patient


class PatientSerializer(serializers.ModelSerializer):

    national_code = serializers.CharField(
        source='user.national_code',
        read_only=True
    )

    first_name = serializers.CharField(
        source='user.first_name',
        read_only=True
    )

    last_name = serializers.CharField(
        source='user.last_name',
        read_only=True
    )

    phone = serializers.CharField(
        source='user.phone',
        read_only=True
    )

    class Meta:
        model = Patient

        fields = [
            'id',
            'national_code',
            'first_name',
            'last_name',
            'phone',
            'birth_date',
            'address',
        ]