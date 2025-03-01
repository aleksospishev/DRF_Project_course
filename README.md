Трекер полезных привычек
Описание:
Это бэкенд-часть SPA веб-приложения, разработанное на DRF, которое способствует приобретению новых полезных привычек и искоренению старых плохих привычек.

Установка, настройка и запуск:
клонировать проект git@github.com:aleksospishev/DRF_Project_course.git


для работы по образцу из env_example создать в корне файл   .env

утанновить зависимости 
pip install -r requirements.txt

Запуск проекта
Примените миграции python3 manage.py migrate.

Запусr локальный серверf командой python3 manage.py runserver.

Запустите брокер сообщений redis-server

Запустите celery celery -A config worker --beat --scheduler django --loglevel=info

