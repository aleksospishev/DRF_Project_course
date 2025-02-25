import requests

from config.settings import TELEGRAM_TOKEN


def send_telegram_message(message, chat_id):
    """Отправка сообщения в telegram."""

    params = {"text": message, "chat_id": chat_id}
    requests.get(
        f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage", params=params
    )
