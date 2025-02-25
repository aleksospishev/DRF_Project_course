from rest_framework import serializers

from habits.models import Habit
from habits.validators import HabitValidator


class HabitSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Привычка"""

    class Meta:
        model = Habit
        fields = "__all__"
        validators = [HabitValidator]
