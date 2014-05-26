import os
from django.core.wsgi import get_wsgi_application
from dj_static import Cling

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'minicra.settings.prod')

application = Cling(get_wsgi_application())