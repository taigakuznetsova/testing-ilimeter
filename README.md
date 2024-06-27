NAFI Project

Описание

Этот проект представляет собой платформу для управления курсами и встречами с использованием Django и PostgreSQL. Он включает в себя регистрацию пользователей, создание и управление встречами, уведомления и многое другое.

Требования

- Python 3.12+
- PostgreSQL
- pip
- virtualenv
- pytest-selenium
- chromedriver 126.0.6478.127 (путь к драйверу pytest -v --driver Chrome --driver-path /path/to//chromedriver.exe)
  

Установка

Шаг 1: Клонирование репозитория

```bash
git clone https://github.com/yourusername/nafi-project.git
cd nafi-project
```
 Шаг 2: Создание и активация виртуального окружения

```bash
python -m venv venv
source venv/bin/activate # Для Windows используйте `venv\Scripts\activate`
```

 Шаг 3: Установка зависимостей

```bash
pip install -r requirements.txt
```

Шаг 4: Настройка базы данных

Убедитесь, что у вас установлен и запущен PostgreSQL. Создайте базу данных и пользователя с правами доступа.

```sql
CREATE DATABASE nafi;
CREATE USER admin WITH PASSWORD 'admin';
ALTER ROLE admin SET client_encoding TO 'utf8';
ALTER ROLE admin SET default_transaction_isolation TO 'read committed';
ALTER ROLE admin SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE nafi TO admin;
```

Настройте параметры подключения к базе данных в файле `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nafi',
        'USER': 'admin',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

Шаг 5: Применение миграций и загрузка данных

Примените миграции для настройки базы данных:

```bash
python manage.py makemigrations
python manage.py migrate
```

```
 Шаг 6: Запуск проекта

Запустите сервер разработки:

```bash
python manage.py runserver
```

Теперь проект доступен по адресу `http://127.0.0.1:8000`.

Шаг 7: Запуск автоматизированных тестов
Запустите драйвер:
pytest -v --driver Chrome --driver-path /path/to//chromedriver.exe

Запустите автотесты auth_tests.py auth_tests_negative.py




