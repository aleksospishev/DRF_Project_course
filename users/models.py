from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Базовая модель пользователя."""

    username = None

    email = models.EmailField(
        max_length=25, unique=True, verbose_name="Почта", help_text="Укажите почту"
    )
    phone = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        verbose_name="Номер телефона",
        help_text="Укажите телефон",
    )
    tg_username = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name="Телеграм ник",
        help_text="Укажите ваш телеграм ник",
    )
    tg_id = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        unique=True,
        verbose_name="Телеграм ID",
        help_text="Укажите ваш телеграм ID",
    )
    city = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name="Город",
        help_text="Укажите номер телефона",
    )
    avatar = models.ImageField(
        upload_to="users/avatar",
        blank=True,
        null=True,
        verbose_name="автар",
        help_text="Ваше фото",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
