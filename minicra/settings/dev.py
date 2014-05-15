from minicra.settings.base import *


WSGI_APPLICATION = 'minicra.wsgi.dev_application'

INSTALLED_APPS += (
    'debug_toolbar.apps.DebugToolbarConfig',
)
