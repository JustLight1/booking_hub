<div align=center>
    
# Приложение Booking Hub

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/fastapi-005571?style=for-the-badge&logo=fastapi)
![SQLAlchemy](https://img.shields.io/badge/sqlalchemy-%23D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=black&logoSize=auto)
![Celery](https://img.shields.io/badge/celery-%233f9429dc?style=for-the-badge&logo=celery&logoSize=auto&labelColor=%233f9429dc)
![Pydantic](https://img.shields.io/badge/Pydantic-black?style=for-the-badge&logo=pydantic&logoColor=red)
![Redis](https://img.shields.io/badge/redis-red?style=for-the-badge&logo=redis&logoSize=auto&color=black)
![Pytest](https://img.shields.io/badge/pytest-black?style=for-the-badge&logo=pytest&logoSize=auto)
![Prometheus](https://img.shields.io/badge/prometheus-black?style=for-the-badge&logo=prometheus&logoSize=auto)
![Grafana](https://img.shields.io/badge/grafana-black?style=for-the-badge&logo=grafana&logoSize=auto)
![Sentry](https://img.shields.io/badge/sentry-black?style=for-the-badge&logo=sentry&logoColor=%23a12a79dc&logoSize=auto)
![Docker](https://img.shields.io/badge/docker-black?style=for-the-badge&logo=docker&logoSize=auto)
![PostgreSQL](https://img.shields.io/badge/postgresql-black?style=for-the-badge&logo=postgresql&logoColor=%232da3f7dc&logoSize=auto)

</div>

## Описание проекта

В данном проекте реализован такой функционал как:

- Редактирование данных через админку и просмотр метрик с помощью Grafana и Prometheus.
- Просмотр отложенных задач Celery с помощью FLower.
- Кеширование данных с помощью Redis.
- Отправка писем на почту по факту бронирования номера.
- Логирование и отображение в Sentry.
- Тестирование кода.
- Контейнеризация с помощью Docker.

Возможности API:

- Пользователи могут зарегистрироваться, авторизоваться, получить свои данные или выйти.
- Работа с пользователями реализована с помощью jwt-токена.
- Пользователи могут: просматривать, создавать или удалять бронирования номеров, а также просматривать отели и номера.

### Технологии

- **Python**

- **FastAPI**: Веб-фреймворк для создания API на Python.
- **SQLAlchemy**: Библиотека для работы с базами данных.
- **Pydantic**: Для валидации данных и сериализации моделей.
- **Alembic**: Инструмент для управления миграциями баз данных.
- **Redis**: Инструмент для кеширования данных и не только.
- **Celery**: Инструмент для работы с отложенными задачами.
- **Flower**: Веб интерфейс для Celery.
- **Pytest**: Библиотека для тестирования.
- **sqladmin**: Библиотека для админки.
- **prometheus**: СУБД для хранения временных рядов, с возможностью построения графиков.
- **Grafana**: Гибкая система визуализации данных с web-интерфейсом.
- **Sentry**: Сервис для просмотра и аналитики ошибок.
- **Docker**: Инструмент для автоматизации развёртывания и управления приложениями с помощью контейнеризации.
- **Uvicorn**: - ASGI веб-сервер для python.
- **PostgreSQL**: - База данных.

<details>

<summary>
<h4>Как запустить проект локально:</h4>
</summary>

Клонировать репозиторий и перейти в него в командной строке:

```bash
git clone git@github.com:JustLight1/booking_hub.git
```

```bash
cd booking_hub
```

Создать и активировать виртуальное окружение:

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

или для пользователей Windows

```bash
source env/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```bash
python3 -m pip install --upgrade pip
```

```bash
pip install -r requirements.txt
```

Создать файл `.env` и заполнить его по примеру из файла `.env.example.dev`

Применить миграции

```bash
alembic upgrade head
```

Запустить проект:

```bash
uvicorn app.main:app --reload
```

После запуска станет доступна документация с доступными запросами и их примерами по адресу:

```
http://localhost:8000/api/v1/docs
```

</details>

<details>

<summary>
<h4>Как запустить проект с помощью docker:</h4>
</summary>

Клонировать репозиторий:

```bash
git clone git@github.com:JustLight1/booking_hub.git
```

Создать файл `.env-non-dev` и заполнить его по примеру из файла `.env-example`

Запустить проект:

- По команде `docker compose up` Docker Compose: получит готовые образы, указанные в `image`, соберёт все образы, указанные в `build`, запустит все контейнеры, описанные в конфиге.
- Флаг `--build` соберет образы.
- Флаг `-d` запустит `docker compose` в режиме демона.

```bash
docker compose up --build -d
```

После запуска станет доступна документация с доступными запросами и их примерами по адресу:

```
http://localhost:8000/api/v1/docs
```

Flower:

```
http://localhost:5555/dashboard
```

Prometheus:

```
http://localhost:9090/
```

Grafana:

```
http://localhost:3000/
```

</details>

# Автор:

**Форов Александр**
[![Telegram Badge](https://img.shields.io/badge/-Light_88-blue?style=social&logo=telegram&link=https://t.me/Light_88)](https://t.me/Light_88) [![Gmail Badge](https://img.shields.io/badge/forov.py@gmail.com-c14438?style=flat&logo=Gmail&logoColor=white&link=mailto:forov.py@gmail.com)](mailto:forov.py@gmail.com)
