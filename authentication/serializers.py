from django.contrib.auth import authenticate

from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

from .models import User


class UserSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "password", "token"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Performs an update on a User."""

        password = validated_data.pop("password", None)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        if password is not None:
            instance.set_password(password)

        instance.save()

        return instance


class LoginSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True, required=True)
    tokens = serializers.JSONField(read_only=True)

    def get_tokens(self, obj):
        user = User.objects.get(username=obj["username"])

        return {"refresh": user.tokens()["refresh"], "access": user.tokens()["access"]}

    def validate(self, data):
        username = data.get("username", None)
        password = data.get("password", None)

        user = authenticate(username=username, password=password)

        if user is None:
            raise AuthenticationFailed("User was not found.")

        if not user.is_active:
            raise AuthenticationFailed("This user has been deactivated.")

        return {
            "id": user.id,
            "username": user.username,
            "tokens": user.tokens,
        }


class LogoutSerializer(serializers.Serializer):
    def __init__(self, instance=None, data=..., **kwargs):
        self.error_messages = {"bad_token": ("Token is expired or invalid")}

        super().__init__(instance, data, **kwargs)
    refresh = serializers.CharField()


    def save(self, **kwargs):
        try:
            RefreshToken(self.data['refresh']).blacklist()
        except TokenError:
            pass
