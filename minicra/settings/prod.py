from minicra.settings.base import *


DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = [
    'minicra.diff-air.com',
]

WSGI_APPLICATION = 'minicra.wsgi-prod.application'
