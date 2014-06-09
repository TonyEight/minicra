from __future__ import unicode_literals
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ContextConfig(AppConfig):
    name = 'business_context'
    verbose_name = _('Business Context Management')
