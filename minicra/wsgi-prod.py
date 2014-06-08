"""
WSGI config for minicra project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""
# Built-in modules
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crm.settings.prod")

# Django modules
from django.core.wsgi import get_wsgi_application


application = get_wsgi_application()
