from __future__ import unicode_literals
from django.contrib import admin
from solo.admin import SingletonModelAdmin
from parameters.models import (
    PublicHoliday,
    SiteConfig
)
from parameters.forms import (
    PublicHolidayAdminForm
)


@admin.register(PublicHoliday)
class PublicHolidayAdmin(admin.ModelAdmin):
    form = PublicHolidayAdminForm


admin.site.register(SiteConfig, SingletonModelAdmin)
