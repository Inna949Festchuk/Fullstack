"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8i#y%va_ymj9d5kymsapxm3)u1e^yce0l^ue1g=c1@%vmsr1o-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Добавление карты сайта. Новый настроечный параметр для ИД
SITE_ID = 1

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin', #сайт администрирования
    'django.contrib.auth', #фреймворк аутентификации
    'django.contrib.contenttypes', #фреймворк типов контента
    'django.contrib.sessions', #фреймворк сеансов
    'django.contrib.messages', #фреймворк сообщений
    'django.contrib.staticfiles', #фреймворк управления статическими файлами
    'blog.apps.BlogConfig', #мое приложение
    # Класс BlogConfig – это конфигурация приложения. Теперь Django знает,
    # что для этого проекта приложение является активным, и сможет загружать
    # модели приложения.
    'taggit', # Добавление функциональности тегирования
    'django.contrib.sites', # Добавление карты сайта. Ассоциация объекты с теми или иными 
    # вебсайтами, работающими вместе с вашим проектом. 
    'django.contrib.sitemaps', # Добавление карты сайта
    'django.contrib.postgres', # Полнотекстовый поиск в PostgreSQL


]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# Переключение базыданных на sqllite3
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# Переключение базыданных на postgresql
# ЭКСПОРТ ДАННЫХ ИЗ СТАРОЙ БД 
# вввести в cmd
# CREATE USER blog WITH PASSWORD 'xxxxxx'; # Введите следующую ниже команду, чтобы создать пользователя, который может создавать базы данных
# CREATE DATABASE blog OWNER blog ENCODING 'UTF8'; # Теперь давайте создадим базу данных blog и передадим права на владение этой базой данных только что созданному пользователю.
# python manage.py dumpdata --indent=2 --output=mysite_data.json # Создание фикстуры
# python -Xutf8 manage.py dumpdata --indent=2 --output=mysite_data.json # Создание фикстуры если возникает ошибка кодировки
DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blog',
        'USER': 'blog',
        'PASSWORD': ':)',
    }
}
# ИМПОРТ ДАННЫХ В НОВУЮ БД 
# Установить драйвер pip install psycopg2
# python manage.py migrate
# Выполните следующую ниже команду, чтобы загрузить данные в базу данных PostgreSQL
# python manage.py loaddata mysite_data.json
# python manage.py runserver

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

# Конфигурация SMTP-сервера Google электронной почты
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'your_account@gmail.com'
# EMAIL_HOST_PASSWORD = '' см. страницу 102
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True

# Если вы не можете использовать SMTP-сервер, то можно сообщить Django,
# что нужно писать электронные письма в консоль, добавив в файл settings.py
# следующий ниже настроечный параметр:
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Откройте оболочку Python, выполнив следующую ниже команду в команд-
# ной строке системной оболочки:
# python manage.py shell
# Исполните следующий ниже исходный код в оболочке Python:
# >>> from django.core.mail import send_mail
# >>> send_mail('Django mail',
# ... 'This e-mail was sent with Django.',
# ... 'your_account@gmail.com',
# ... ['your_account@gmail.com'],
# ... fail_silently=False)
# Функция send_mail() принимает тему, сообщение, отправителя и список
# получателей в качестве требуемых аргументов. Устанавливая опциональный
# аргумент fail_silently=False, мы сообщаем ей, что если электронное письмо
# невозможно отправить, нужно вызывать исключение. Если результат, кото-
# рый вы видите, равен 1, значит, ваше электронное письмо было успешно
# отправлено.
# Проверьте свой почтовый ящик. Вы должны были получить электронное
# письмо:
# Давайте добавим эту функциональность в представление post_share.

# Отправка электронных писем в представлениях (идем в views.py)
# Отредактируйте представление post_share в файле views.py приложения blog,
# как показано ниже: