from django.core.validators import MaxValueValidator
from django.db import models

from users.models import User


class Habit(models.Model):
    habit = models.CharField(max_length=100, verbose_name="Привычка- действие")
    place_of_event = models.CharField(
        max_length=100, verbose_name="Место выполнения привычки", blank=True, null=True
    )
    time_of_event = models.TimeField(
        verbose_name="Время когда выполнять привычку", blank=True, null=True
    )
    periodicity = models.IntegerField(
        validators=(MaxValueValidator(7),),
        verbose_name="Переодичность привычки",
        default=1,
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="owner_habit",
        blank=True,
        null=True,
    )
    nice_habit = models.BooleanField(
        default=False, verbose_name="Признак приятной привычки"
    )
    related_habit = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        verbose_name="Связаная привычка",
        related_name="related_habits",
        blank=True,
        null=True,
    )
    reward = models.CharField(
        max_length=250, verbose_name="Вознаграждение", blank=True, null=True
    )
    time_to_complete = models.IntegerField(
        default=60,
        validators=(MaxValueValidator(120),),
    )
    published = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
        ordering = ("id",)

    def __str__(self):
        return self.habit
