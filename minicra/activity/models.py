import datetime
import calendar
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from context.models import Contract


class Activity(models.Model):
    PERIODS = (
        (1, 'morning'),
        (2, 'afternoon'),
        (3, 'all_day'),
    )
    date = models.DateField()
    period = models.PositiveIntegerField(
        choices=PERIODS,
        default=3
    )
    contract = models.ForeignKey(
        Contract,
        related_name='activities'
    )
    comment = models.TextField(
        blank=True
    )

    class Meta:
        verbose_name = _('Activity')
        verbose_name_plural = _('Activities')

    def __unicode__(self):
        return u'%s: %s (%s)' % (self.contract.actor, self.date, self.get_period_display())


class OffDay(models.Model):
    PERIODS = (
        (1, 'morning'),
        (2, 'afternoon'),
        (3, 'all_day'),
    )
    date = models.DateField()
    period = models.PositiveIntegerField(
        choices=PERIODS,
        default=3
    )
    contract = models.ForeignKey(
        Contract,
        related_name='off_days'
    )
    comment = models.TextField(
        blank=True
    )

    class Meta:
        verbose_name = _('Off Day')
        verbose_name_plural = _('Off Days')

    def __unicode__(self):
        return u'%s: %s (%s)' % (self.contract.actor, self.date, self.get_period_display())


def get_month_list():
    months = ()
    for i in range(1, 13):
        months.append(
            (i, calendar.month_name[i])
        )
    return months

class Report(models.Model):
    MONTHS = (
        (1, calendar.month_name[1]),
        (2, calendar.month_name[2]),
        (3, calendar.month_name[3]),
        (4, calendar.month_name[4]),
        (5, calendar.month_name[5]),
        (6, calendar.month_name[6]),
        (7, calendar.month_name[7]),
        (8, calendar.month_name[8]),
        (9, calendar.month_name[9]),
        (10, calendar.month_name[10]),
        (11, calendar.month_name[11]),
        (12, calendar.month_name[12]),
    )
    month = models.PositiveIntegerField(
        choices=MONTHS
    )
    year = models.PositiveIntegerField(default=datetime.datetime.now().year)
    worked_days = models.PositiveIntegerField(editable=False, default=0)
    off_days = models.PositiveIntegerField(editable=False, default=0)
    days_with_activity = models.PositiveIntegerField(editable=False, default=0)
    contract = models.ForeignKey(
        Contract,
        related_name='activity_reports'
    )    

    class Meta:
        verbose_name = _('Report')
        verbose_name_plural = _('Reports')
        unique_together = ('contract', 'month', 'year')

    def __unicode__(self):
        return u'Activity Report of %s %d' % (self.get_month_display(), self.year)

    def save(self, *args, **kwargs):
        c = calendar.Calendar()
        weekdays = 0
        for d in c.itermonthdays2(self.year, self.month):
            if d[0] != 0 and d[1] not in [5, 6]:
                weekdays += 1
        self.worked_days = weekdays
        activities = 0
        for a in Activity.objects.filter(date__year=self.year, date__month=self.month, contract=self.contract):
            if a.period == 3:
                activities += 1
            else:
                activities += 0.5
        self.days_with_activity = activities
        off_days = 0
        for a in OffDay.objects.filter(date__year=self.year, date__month=self.month, contract=self.contract):
            if a.period == 3:
                off_days += 1
            else:
                off_days += 0.5
        self.off_days = off_days
        super(Report, self).save(*args, **kwargs)
