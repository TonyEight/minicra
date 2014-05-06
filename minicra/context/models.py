from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class Organisation(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True
    )

    class Meta:
        verbose_name = _('Organisation')
        verbose_name_plural = _('Organisations')

    def __unicode__(self):
        return self.name
    

class Client(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True
    )
    service = models.CharField(
        max_length=200,
    )
    organisation = models.ForeignKey(
        Organisation
    )

    class Meta:
        verbose_name = _('Client')
        verbose_name_plural = _('Clients')

    def __unicode__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(
        max_length=260
    )

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')

    def __unicode__(self):
        return self.name


class Contract(models.Model):
    mission = models.CharField(
        max_length=260
    )
    description = models.TextField(
        blank=True
    )
    project = models.ForeignKey(
        Project
    )
    client = models.ForeignKey(
        Client
    )
    actor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='contracts'
    )
    start = models.DateField(
    )
    end = models.DateField(
        blank=True
    )
    sold_days = models.PositiveIntegerField(
        blank=True
    )
    distribution = models.PositiveIntegerField(
        blank=True
    )

    class Meta:
        verbose_name = _('Contract')
        verbose_name_plural = _('Contracts')

    def __unicode__(self):
        return self.mission
    