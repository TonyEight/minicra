"""
WSGI config for minicra project.

Caution: the default behavior has been replaced to manager each environment 
settings module.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""
# Built-in modules
import os
# Django modules
from django.core.wsgi import get_wsgi_application
from django.conf import settings

def get_wsgi_app(env):
    settings_module = 'minicra.settings.%s' % env
    settings.SETTINGS_MODULE = __import__(settings_module)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)
    return get_wsgi_application()

dev_application = get_wsgi_app('dev')
application = dev_application
prod_application = get_wsgi_app('prod')
