# Habit Tracker — трекер полезных привычек

Проект реализован как backend-часть SPA-приложения по книге Джеймса Клира «Атомные привычки». Сервис помогает пользователям формировать полезные привычки, отслеживать их выполнение и получать напоминания через Telegram.

## Функциональность

- JWT-аутентификация и регистрация пользователей
- CRUD для привычек с различными типами (полезные/приятные)
- Telegram-напоминания о привычках через Celery + Redis
- Публичные привычки доступны другим пользователям
- Пагинация (по 5 привычек на страницу)
- Валидация бизнес-логики (время ≤ 2 мин, связность привычек и др.)
- Покрытие тестами 
- CORS для SPA-интерфейса
- Контейнеризация (Django, PostgreSQL, Redis, Celery, Nginx)
- CI/CD: автодеплой через GitHub Actions

## Технологии

- Python 3.12
- Django, Django REST Framework
- PostgreSQL
- Celery + Redis
- Telegram Bot API
- Docker, Docker Compose, Nginx
- GitHub Actions
- pytest, coverage, flake8

## Установка локально

### 1. Клонирование

```bash
git clone https://github.com/aleksospishev/DRF_Project_course.git
cd DRF_Project_course
```

### 2. Переменные окружения
Создайте в корне .env заполните по примеру env_example:

 ### 3. Запуск проекта

```bash
docker-compose up --build
```
- Сервис будет доступен по адресу:
  http://localhost/
- Документация API (Swagger):
  http://localhost/api/docs/

## Telegram-уведомления
В проекте реализована интеграция с Telegram-ботом. Напоминания о привычках отправляются через отложенные задачи (Celery)

- Запуск воркера:
```bash
docker-compose exec web celery -A config worker -l info
```
- Запуск beat (для периодических задач):

```bash
docker-compose exec web celery -A config beat -l info
```

## Эндпоинты

| Метод | URL                         | Описание                             |
|--------|-----------------------------|--------------------------------------|
| POST   | /api/register/              | Регистрация                          |
| POST   | /api/token/                 | Авторизация (JWT)                    |
| GET    | /api/habits/                | Список привычек текущего пользователя |
| GET    | /api/habits/public/         | Список публичных привычек            |
| POST   | /api/habits/                | Создание привычки                    |
| PUT    | /api/habits/<id>/           | Редактирование привычки              |
| DELETE | /api/habits/<id>/           | Удаление привычки                    |

## Тестирование
```bash
docker-compose exec web pytest --cov
```

## CI/CD
При пуше в git:

- Проверяется PEP8 (flake8)

- Прогоняются тесты (pytest)

- Сборка Docker-образов

- Автодеплой на сервер по SSH

- Конфигурация в .github/workflows/
    Автоматический деплой требует настройки SSH-секрета задаются в GitHub Secrets.

| Переменная            | Описание                                 |
|-----------------------|------------------------------------------|
| `SECRET_KEY`          | Секретный ключ Django проекта            |
| `DOCKER_PASSWORD`     | Пароль от Docker Hub                     |
| `DOCKER_USERNAME`     | Логин Docker Hub                         |
| `HOST`                | Публичный IP сервера                     |
| `USER`                | Имя пользователя на сервере              |
| `PASSPHRASE`          | Пароль к SSH-ключу (если установлен)     |
| `SSH_KEY`             | Приватный SSH-ключ                       |
| `DB_NAME`             | Имя базы данных                          |
| `POSTGRES_USER`       | Пользователь базы данных                 |
| `POSTGRES_PASSWORD`   | Пароль от базы данных                    |
| `DB_HOST`             | Хост базы данных (например, `db`)        |
| `DB_PORT`             | Порт базы данных (по умолчанию: `5432`)  |


## Права доступа

- Пользователь имеет доступ только к своим привычкам

- Публичные привычки доступны на чтение для всех

- Приятные привычки не могут иметь награды или связанные привычки

## Стандарты
- 100% Flake8 (исключая миграции)

- Использование переменных окружения

- Документация к API

Автор  
Александр Оспищев — Python-разработчик  
aleksospishev@gmail.com  
GitHub: aleksospishev


