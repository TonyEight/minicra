# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('business_context', '0002_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mission', models.CharField(max_length=260)),
                ('description', models.TextField(null=True, blank=True)),
                ('project', models.CharField(max_length=260, null=True, blank=True)),
                ('client', models.ForeignKey(to='business_context.Client', to_field='id')),
                ('actor', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id')),
                ('start', models.DateField()),
                ('end', models.DateField(null=True, blank=True)),
                ('sold_days', models.PositiveIntegerField(null=True, blank=True)),
                ('distribution', models.PositiveIntegerField(null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Contract',
                'verbose_name_plural': 'Contracts',
            },
            bases=(models.Model,),
        ),
    ]
