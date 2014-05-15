from django.contrib import admin
from activity.models import (
    DeclaredDay,
    Report,
)


class DeclaredDayAdmin(admin.ModelAdmin):
    list_display = ('date', 'contract', 'actor', 'type', 'period',)
    list_display_links = ('date',)
    list_filter = ('type', 'period', 'contract', 'contract__actor',)


class ReportAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'contract', 'worked_days', 'off_days',
                    'days_with_activity',)


admin.site.register(DeclaredDay, DeclaredDayAdmin)
admin.site.register(Report, ReportAdmin)
