from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from solo.models import SingletonModel


class FixedPublicHolidayManager(models.Manager):
    def get_queryset(self):
        return super(FixedPublicHolidayManager, self).get_queryset()\
                                                     .filter(is_fixed=True)


class NonFixedPublicHolidayManager(models.Manager):
    def get_queryset(self):
        return super(NonFixedPublicHolidayManager, self).get_queryset()\
                                                        .filter(
                                                            is_fixed=False)


class PublicHolidayQuerySet(models.QuerySet):
    def for_month(self, month, year):
        return self.filter(
            models.Q(is_fixed=True, month=month) |
            models.Q(is_fixed=False, month=month, year=year)
        )


class PublicHolidayManager(models.Manager):
    def get_queryset(self):
        return PublicHolidayQuerySet(self.model, using=self._db)

    def for_month(self, month, year):
        return self.get_queryset().for_month(month=month, year=year)


class PublicHoliday(models.Model):
    name = models.CharField(max_length=255, unique=True)
    day = models.PositiveIntegerField()
    month = models.PositiveIntegerField()
    year = models.PositiveIntegerField(blank=True, null=True)
    is_fixed = models.BooleanField(default=True)

    objects = PublicHolidayManager()
    fixed_objects = FixedPublicHolidayManager()
    nonfixed_objects = NonFixedPublicHolidayManager()

    class Meta:
        verbose_name = _('Public Holiday')
        verbose_name_plural = _('Public Holidays')
        ordering = ('is_fixed', 'year', 'month', 'day',)

    def __unicode__(self):
        year = ''
        if self.year:
            year = '/%.2d' % self.year
        return '%s (%.2d/%.2d%s)' % (self.name, self.day, self.month, year)


class SiteConfig(SingletonModel):
    site_name = models.CharField(max_length=255, default='MiniCRA')
    icon_CSS_class = models.CharField(max_length=255,
                                      default='glyphicon glyphicon-stats')

    class Meta:
        verbose_name = 'Site Configuration'
        verbose_name_plural = 'Site Configuration'

    def __unicode__(self):
        return 'Site Configuration'
