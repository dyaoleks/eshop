DEBUG = True           # щоб не видавалися повідомлення про помилки
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'eshop',
        'USER': 'eshop',
        'PASSWORD': '607C0BAB5CD273F7EB8FE1C098B9EC20B58EDE578A326E1C9E98C591B3EAD053',
        'HOST': 'localhost',
        'PORT': '',     # за замовчуванням
    }
}