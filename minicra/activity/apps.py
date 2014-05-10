from django.apps import AppConfig


class ActivityConfig(AppConfig):
    name = 'activity'
    verbose_name = 'MiniCRA - Activity Management'

    def ready(self):
    	from activity import signals