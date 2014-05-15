import datetime
import calendar
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from business_context.models import Contract


class DeclaredDay(models.Model):
    PERIODS = (
        (1, 'Morning'),
        (2, 'Afternoon'),
        (3, 'Whole day'),
    )
    TYPES = (
        (1, 'Activity'),
        (2, 'Off Day'),
    )
    date = models.DateField()
    period = models.PositiveIntegerField(
        choices=PERIODS,
        default=1
    )
    type = models.PositiveIntegerField(
        choices=TYPES,
        default=3
    )
    contract = models.ForeignKey(
        Contract,
        related_name='declared_days'
    )
    comment = models.TextField(
        blank=True
    )

    class Meta:
        verbose_name = _('Activity')
        verbose_name_plural = _('Activities')
        ordering = ('date', 'contract',)

    def _get_actor(self):
        return self.contract.actor
    actor = property(_get_actor)

    def __unicode__(self):
        return u'%s: %s (%s)' % (self.date, self.contract,
                                 self.get_period_display())


class Month(models.Model):
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

    class Meta:
        verbose_name = _('Month')
        verbose_name_plural = _('Months')
        unique_together = ('month', 'year')

    def __unicode__(self):
        return u'%s %s' % (self.get_month_display(), self.year)

    def dates_list(self):
        c = calendar.Calendar()
        dates = []
        for d in c.itermonthdays2(self.year, self.month):
            if d[0] != 0:
                dates.append((d[0], d[1], calendar.day_name[d[1]]))
        return dates

    def save(self, *args, **kwargs):
        c = calendar.Calendar()
        weekdays = 0
        for d in c.itermonthdays2(self.year, self.month):
            if d[0] != 0 and d[1] not in [5, 6]:
                weekdays += 1
        self.worked_days = weekdays
        super(Month, self).save(*args, **kwargs)


class Report(models.Model):
    off_days = models.FloatField(editable=False, default=0.0)
    days_with_activity = models.FloatField(editable=False, default=0.0)
    month = models.ForeignKey(
        Month,
        related_name='activity_reports'
    )
    contract = models.ForeignKey(
        Contract,
        related_name='activity_reports'
    )

    class Meta:
        verbose_name = _('Report')
        verbose_name_plural = _('Reports')
        unique_together = ('contract', 'month')

    def __unicode__(self):
        return u'Activity Report of %s' % (self.month)

    @classmethod
    def get_reports_for(cls, user):
        return cls.objects.filter(contract__actor=user)

    def _get_worked_days(self):
        return self.month.worked_days
    worked_days = property(_get_worked_days)

    def save(self, *args, **kwargs):
        c = calendar.Calendar()
        activities = 0
        for act in DeclaredDay.objects.filter(
            type=1,
            date__year=self.month.year,
            date__month=self.month.month,
            contract=self.contract
        ):
            if act.period == 3:
                activities += 1
            else:
                activities += 0.5
        self.days_with_activity = activities
        off_days = 0
        for off in DeclaredDay.objects.filter(
            type=2,
            date__year=self.month.year,
            date__month=self.month.month,
            contract=self.contract
        ):
            if off.period == 3:
                off_days += 1
            else:
                off_days += 0.5
        self.off_days = off_days
        super(Report, self).save(*args, **kwargs)
