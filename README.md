Трекер полезных привычек
Описание:
Это бэкенд-часть SPA веб-приложения, разработанное на DRF, которое способствует приобретению новых полезных привычек и искоренению старых плохих привычек.

Установка, настройка и запуск:
подготовить сервер к развертыванию проекта, установить docker, docker compose
на сервер клонировать проект git@github.com:aleksospishev/DRF_Project_course.git

заполнить файл .env по примеру env_example

скачать актуальную версию докер-образа проекта
"""sudo docker pull aleksospishev/habits_project:latest"""

запустить проект
"""sudo docker compose up -d"""

установить миграции 
"""sudo docker compose exec -T web python manage.py migrate"""

запустить
"""sudo docker compose exec -T web python manage.py runserver"""

