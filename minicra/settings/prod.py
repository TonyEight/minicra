from minicra.settings.base import *


DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = [
    '*',
]

WSGI_APPLICATION = 'minicra.wsgi.prod_application'

import dj_database_url
DATABASES['default'] =  dj_database_url.config()

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'static'),
)