from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import *


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'username')


class ProfileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number')


class UserRegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = Profile
        fields = ('username', 'email', 'password1', 'password2')

    def validate_password(self, value):
        validate_password(value)
        return value

    # Валидация паролей на совпадения
    def validate(self, data):
        # Проверяем, что оба пароля совпадают
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(_({"password": "Passwords don't match"}))
        return data

    def create(self, validated_data):
        # Убираем password2 из данных, т.к. он больше не нужен
        validated_data.pop('password2')
        # Используем password1 как пароль пользователя
        password = validated_data.pop('password1')
        user = Profile.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=password
        )
        Token.objects.create(user=user)
        return user


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField()
    confirm_new_password = serializers.CharField()


class ResetPasswordEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()

