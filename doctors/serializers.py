from rest_framework import serializers

from .models import Doctor, Specialty


class SpecialtySerializer(serializers.ModelSerializer):

    class Meta:
        model = Specialty
        fields = [
            'id',
            'name',
        ]


class DoctorSerializer(serializers.ModelSerializer):

    first_name = serializers.CharField(
        source='user.first_name',
        read_only=True
    )

    last_name = serializers.CharField(
        source='user.last_name',
        read_only=True
    )

    national_code = serializers.CharField(
        source='user.national_code',
        read_only=True
    )

    specialty_name = serializers.CharField(
        source='specialty.name',
        read_only=True
    )

    class Meta:
        model = Doctor
        fields = [
            'id',
            'first_name',
            'last_name',
            'national_code',
            'specialty',
            'specialty_name',
            'city',
            'area',
            'experience',
            'bio',
            'image',
            'rating',
            'is_active',
        ]