from __future__ import unicode_literals
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from activity.models import (
    DeclaredDay,
    Month,
    Report
)


@receiver(post_save, sender=DeclaredDay)
@receiver(post_delete, sender=DeclaredDay)
def generate_report_from_activity(sender, instance, **kwargs):
    month, m_created = Month.objects.get_or_create(
        month=instance.date.month,
        year=instance.date.year
    )
    report, created = Report.objects.get_or_create(
        month=month,
        contract=instance.contract
    )
    report.save()
