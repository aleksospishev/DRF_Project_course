import datetime

from celery import shared_task

from habits.models import Habit
from habits.services import send_telegram_message


@shared_task
def send_habit():
    habits = Habit.objects.all()
    current_date = datetime.datetime.now()  # Текущее время
    for habit in habits:
        if habit.time_of_event >= current_date:
            tg_chat = habit.user.tg_id
            message = f"Я буду {habit.habit} в {habit.time_of_event} в {habit.place_of_event}."
            send_telegram_message(
                tg_chat, message
            )  # Отправляем привычку в Telegram чат
