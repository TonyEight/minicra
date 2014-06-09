from __future__ import unicode_literals
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ActivityConfig(AppConfig):
    name = 'activity'
    verbose_name = _('Activity Management')

    def ready(self):
        from activity import signals
