from django.contrib import admin
from context.models import (
    Organisation,
    Client,
    Contract,
    Project
)

admin.site.register(Organisation)
admin.site.register(Client)
admin.site.register(Contract)
admin.site.register(Project)
