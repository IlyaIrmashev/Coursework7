from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор пользователя"""
    class Meta:
        model = User
        fields = ('id', 'username', 'tg_user_id', 'last_name', 'is_active', 'password')


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super().create(validated_data)

    class Meta:
        model = User
        fields = ['username', 'password', 'tg_user_id']
