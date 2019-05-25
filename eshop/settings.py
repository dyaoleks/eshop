"""
Django settings for ELIB project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ----------------------------------------------------
# цікаві налаштування, що треба ПЕРЕВІРИТИ

ADMINS = ('oleksandr_diadiushenko', 'dyaole@gmail.com'),
MANAGERS = ADMINS

# --------------------------------------------------------

# ADMIN_SITE_HEADER = "My shiny new administration"




# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 't)i+wqo@p7k!ong$s&et2aa9uw8bkmq3(9!$eu4eefi_j@ev*!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [ ]



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'shop',
    # 'distance',
    # 'login',
    # 'lit',
    # 'masters',
    # 'publications',
    #
    #
    # #external packages
    # 'import_export',
    # 'dbbackup',  # django-dbbackup тестова бібліотека для створення резервних копій з бази даних
    # 'django_archive',
    # 'crispy_forms',
    # 'dropbox',
    # 'online_users',
    #     # 'django_summernote',
]

CRISPY_TEMPLATE_PACK = "bootstrap4"


# DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
# DBBACKUP_STORAGE_OPTIONS = {'location': '/webapps/elib/elib/BACKUPS'}


# DEFAULT_FILE_STORAGE = 'storages.backends.dropbox.DropBoxStorage'
#
# DBBACKUP_STORAGE = 'storages.backends.dropbox.DropBoxStorage'
# DBBACKUP_STORAGE_OPTIONS = {
#     'oauth2_access_token': 'Em_GB23eW9AAAAAAAAAE9SZICfBC-dyyO9x6RvG7UBbVKiejnYpVwSf1ys3qNQR3',
# }




# ARCHIVE_DIRECTORY = 'C:/Users/Oleksandr/Dropbox/Other/ARCHIVE/eLib'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # 'online_users.middleware.OnlineNowMiddleware',

]

ROOT_URLCONF = 'eshop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'eshop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'Uk-uk'

TIME_ZONE = 'Europe/Istanbul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
  os.path.join(BASE_DIR, "static", "static_dev"),
)

STATIC_ROOT = os.path.join(BASE_DIR, "static", "static_prod")

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, "static", "media")

FILE_UPLOAD_MAX_MEMORY_SIZE = 200000000

# uncomment (налаштування для запуску серверу на убунту)
# try:
#     from .settings_prod import *
# except:
#     pass
