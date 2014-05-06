from django.contrib import admin
from activity.models import (
    Activity,
    OffDay,
    Report,
)

class ReportAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'contract', 'worked_days', 'off_days', 'days_with_activity')

admin.site.register(Activity)
admin.site.register(OffDay)
admin.site.register(Report, ReportAdmin)
