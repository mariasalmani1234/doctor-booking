from rest_framework import serializers
from .models import User
from patients.models import Patient


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        min_length=8
    )

    confirm_password = serializers.CharField(
        write_only=True
    )

    class Meta:
        model = User
        fields = [
            'national_code',
            'first_name',
            'last_name',
            'phone',
            'email',
            'password',
            'confirm_password',
        ]

    def validate_national_code(self, value):
        if not value.isdigit():
            raise serializers.ValidationError(
                'کد ملی باید فقط شامل عدد باشد.'
            )

        if len(value) != 10:
            raise serializers.ValidationError(
                'کد ملی باید ۱۰ رقم باشد.'
            )

        if User.objects.filter(national_code=value).exists():
            raise serializers.ValidationError(
                'این کد ملی قبلاً ثبت شده است.'
            )

        return value

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError(
                {
                    'confirm_password':
                    'رمز عبور و تکرار آن یکسان نیستند.'
                }
            )

        return attrs

    def create(self, validated_data):

        validated_data.pop('confirm_password')

        password = validated_data.pop('password')

        user = User(
            username=validated_data['national_code'],
            role=User.Role.PATIENT,
            **validated_data
        )

        user.set_password(password)
        user.save()

        Patient.objects.create(
            user=user
        )

        return user