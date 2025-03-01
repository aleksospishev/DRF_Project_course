from django.contrib import admin

from habits.models import Habit


@admin.register(Habit)
class HabitsAdmin(admin.ModelAdmin):
    list_display = ["pk", "owner", "place_of_event", "time_of_event", "habit"]
