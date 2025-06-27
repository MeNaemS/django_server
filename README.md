# 🛒 Django Order Management System

Система управления заказами на Django с административной панелью для управления товарами, категориями, заказами и пользователями.

## 📋 Содержание

- [Особенности](#-особенности)
- [Технологии](#-технологии)
- [Структура проекта](#-структура-проекта)
- [Установка и запуск](#-установка-и-запуск)
- [Конфигурация](#️-конфигурация)
- [Использование](#-использование)
- [Разработка](#-разработка)
- [Docker](#-docker)
- [Безопасность](#-безопасность)
- [Лицензия](#-лицензия)

## ✨ Особенности

- 🏪 **Управление товарами**: Создание, редактирование и удаление товаров с изображениями
- 📂 **Категории**: Иерархическая система категорий с поддержкой подкатегорий
- 🛍️ **Корзина**: Функционал корзины покупок для пользователей
- 📦 **Заказы**: Полный цикл обработки заказов от создания до выполнения
- 👥 **Пользователи**: Система подписок и управления пользователями
- 📢 **Рассылки**: Система широковещательных сообщений
- ❓ **FAQ**: Раздел часто задаваемых вопросов
- 🎨 **Админ-панель**: Полнофункциональная административная панель Django

## 🛠 Технологии

- **Backend**: Django 5.2.3, Python 3.13
- **База данных**: PostgreSQL
- **ASGI сервер**: Uvicorn 0.34.3
- **Конфигурация**: Dynaconf 3.2.11
- **Статические файлы**: WhiteNoise 6.9.0
- **Изображения**: Pillow 11.2.1
- **Контейнеризация**: Docker & Docker Compose

## 📁 Структура проекта

```text
DjangoServer/
├── 📄 Dockerfile                # Docker конфигурация
├── 📄 requirements.txt          # Python зависимости
├── 📄 LICENSE                   # MIT лицензия
├── 📁 configs/                  # Конфигурационные файлы
│   ├── config.toml              # Основная конфигурация
│   └── secret.toml              # Секретные настройки (не в git)
└── 📁 order_system/             # Основное Django приложение
    ├── 📄 manage.py             # Django management команды
    ├── 📄 configs.py            # Загрузка конфигурации
    ├── 📄 configs_schema.py     # Схема конфигурации
    ├── 📁 admin/                # Django проект настройки
    │   ├── settings.py          # Настройки Django
    │   ├── urls.py              # URL маршруты
    │   ├── wsgi.py              # WSGI конфигурация
    │   └── asgi.py              # ASGI конфигурация
    ├── 📁 management/           # Основное приложение
    │   ├── admin.py             # Админ панель
    │   ├── apps.py              # Конфигурация приложения
    │   ├── models/              # Модели данных
    │   │   ├── admin.py         # Модели администрирования
    │   │   ├── order_cart.py    # Модели заказов и корзины
    │   │   ├── products.py      # Модели товаров
    │   │   └── subscribe.py     # Модели подписок и FAQ
    │   └── migrations/          # Миграции базы данных
    └── 📁 static/               # Статические файлы
        └── admin/               # Статика админ панели
```

## 🚀 Установка и запуск

### Предварительные требования

- Docker и Docker Compose
- Git

### Быстрый старт

1. **Клонирование репозитория**

   ```bash
   git clone <repository-url>
   cd DjangoServer
   ```

2. **Создание файла с секретами**

   ```bash
   # Создайте файл configs/secret.toml
   cp configs/config.toml configs/secret.toml
   ```

   Отредактируйте `configs/secret.toml`:

   ```toml
   [default.database]
   user = "your_db_user"
   password = "your_db_password"
   name = "your_db_name"
   
   [default.django]
   secret_key = "your-secret-django-key"
   ```

3. **Запуск с Docker Compose**

   ```bash
   # Создание и запуск контейнеров
   docker compose up -d
   
   # Применение миграций
   docker compose exec web python manage.py migrate
   
   # Создание суперпользователя
   docker compose exec web python manage.py createsuperuser
   
   # Сбор статических файлов
   docker compose exec web python manage.py collectstatic --noinput
   ```

4. **Доступ к приложению**
   - Основное приложение: <http://localhost:8000>
   - Админ панель: <http://localhost:8000/admin/>

### Альтернативный запуск (без Docker)

1. **Установка зависимостей**

   ```bash
   pip install -r requirements.txt
   ```

2. **Настройка базы данных PostgreSQL**

   ```bash
   # Создайте базу данных PostgreSQL
   createdb your_db_name
   ```

3. **Применение миграций**

   ```bash
   cd order_system
   python manage.py migrate
   python manage.py createsuperuser
   ```

4. **Запуск сервера**

   ```bash
   # Разработка
   python manage.py runserver
   
   # Продакшн с Uvicorn
   uvicorn admin.asgi:application --host 0.0.0.0 --port 8000
   ```

## ⚙️ Конфигурация

Система использует **Dynaconf** для управления конфигурацией с поддержкой различных окружений.

### Файлы конфигурации

- `configs/config.toml` - основные настройки
- `configs/secret.toml` - секретные данные (не добавляется в git)

### Окружения

- `default` - настройки по умолчанию
- `production` - продакшн настройки

### Переменные окружения

```bash
ENV_FOR_DYNACONF=production  # Выбор окружения
```

### Пример конфигурации

```toml
[default]
log_level = "DEBUG"
debug = true

[default.database]
host = "localhost"
port = 5432
user = "postgres"
password = "password"
name = "order_system"

[default.django]
secret_key = "your-secret-key-here"

[production]
log_level = "WARNING"
debug = false

[production.database]
host = "postgres"  # Docker service name
```

## 📖 Использование

### Административная панель

1. Войдите в админ панель: <http://localhost:8000/admin/>
2. Используйте созданные учетные данные суперпользователя

### Основные модели

#### 🏷️ Категории (Categories)

- Создание иерархических категорий товаров
- Поддержка подкатегорий

#### 📦 Товары (Products)

- Название, описание, цена
- Загрузка изображений
- Привязка к категориям

#### 🛒 Корзина (Cart)

- Управление товарами в корзине
- Количество товаров

#### 📋 Заказы (Orders)

- Информация о клиенте
- Состав заказа
- Способ оплаты

#### 👤 Подписки (UserSubscription)

- Управление подписками пользователей

#### 📢 Рассылки (BroadcastMessage)

- Создание сообщений для рассылки
- Отслеживание статуса отправки

#### ❓ FAQ

- Часто задаваемые вопросы и ответы

### Команды управления

```bash
# Создание миграций
python manage.py makemigrations

# Применение миграций
python manage.py migrate

# Создание суперпользователя
python manage.py createsuperuser

# Сбор статических файлов
python manage.py collectstatic

# Запуск сервера разработки
python manage.py runserver
```

## 🔧 Разработка

### Структура моделей

Модели организованы в отдельные файлы по функциональности:

- `models/admin.py` - административные модели
- `models/products.py` - товары и категории
- `models/order_cart.py` - заказы и корзина
- `models/subscribe.py` - подписки и FAQ

### Добавление новых функций

1. Создайте новые модели в соответствующем файле
2. Зарегистрируйте модели в `admin.py`
3. Создайте и примените миграции
4. Обновите документацию

### Тестирование

```bash
# Запуск тестов
python manage.py test

# Запуск с покрытием
coverage run --source='.' manage.py test
coverage report
```

### Логирование

Система использует стандартное логирование Django. Уровень логирования настраивается в конфигурации:

```toml
[default]
log_level = "DEBUG"  # DEBUG, INFO, WARNING, ERROR, CRITICAL
```

## 🐳 Docker

### Dockerfile

Приложение использует Python 3.13-slim образ с оптимизированной конфигурацией для продакшн.

### Docker Compose

Для полного стека с PostgreSQL используйте docker-compose:

```yaml
version: '3.8'
services:
  web:
    build: .
    ports:
      - "8000:8000"
    depends_on:
      - postgres
    environment:
      - ENV_FOR_DYNACONF=production
  
  postgres:
    image: postgres:15
    environment:
      POSTGRES_DB: order_system
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: password
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

## 🔒 Безопасность

- Секретные данные хранятся в отдельном файле `secret.toml`
- Используется Django CSRF защита
- Настроены безопасные заголовки
- Статические файлы обслуживаются через WhiteNoise

## 📝 Лицензия

Этот проект лицензирован под MIT License - см. файл [LICENSE](LICENSE) для деталей.
