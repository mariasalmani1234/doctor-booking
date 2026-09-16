from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        min_length=8
    )
    password_confirm = serializers.CharField(
        write_only=True
    )
    class Meta:
        model = User

        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'phone',
            'password',
            'password_confirm',
        ]

    def validate(self, attrs):

        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError({
                'password_confirm': 'رمز عبور و تکرار آن یکسان نیست.'
            })

        return attrs

    def create(self, validated_data):

        validated_data.pop('password_confirm')
        password = validated_data.pop('password')
        user = User.objects.create_user(
            password=password,
            **validated_data
        )

        return user