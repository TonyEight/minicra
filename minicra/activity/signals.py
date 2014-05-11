from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from activity.models import (
    Activity,
    OffDay,
    Month, 
    Report
)

@receiver(post_save, sender=Activity)
@receiver(post_delete, sender=Activity)
def generate_report_from_activity(sender, instance, **kwargs):
    month, m_created = Month.objects.get_or_create(
        month = instance.date.month,
        year = instance.date.year
    )
    report, created = Report.objects.get_or_create(
        month = month,
        contract = instance.contract
    )
    report.save()

@receiver(post_save, sender=OffDay)
@receiver(post_delete, sender=OffDay)
def generate_report_from_offday(sender, instance, **kwargs):
    month, m_created = Month.objects.get_or_create(
        month = instance.date.month,
        year = instance.date.year
    )
    report, created = Report.objects.get_or_create(
        month = month,
        contract = instance.contract
    )
    report.save()