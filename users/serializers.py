from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Сериализация пользователя."""

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "phone",
            "tg_username",
            "tg_id",
            "city",
            "avatar",
            "is_active",
            "password",
        )
