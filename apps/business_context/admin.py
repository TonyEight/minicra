from __future__ import unicode_literals
from django.contrib import admin
from business_context.models import (
    Organisation,
    Client,
    Contract
)

admin.site.register(Organisation)
admin.site.register(Client)
admin.site.register(Contract)
