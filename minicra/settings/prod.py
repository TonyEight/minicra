from minicra.settings.base import *


DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = [
    'minicra.diff-air.com',
]

WSGI_APPLICATION = 'minicra.wsgi.prod_application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
