# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteConfig',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                 serialize=False, auto_created=True, primary_key=True)),
                ('site_name',
                 models.CharField(default=b'MiniCRA', max_length=255)),
                ('icon_CSS_class', models.CharField(
                    default=b'glyphicon glyphicon-stats', max_length=255)),
            ],
            options={
                'verbose_name': b'Site Configuration',
                'verbose_name_plural': b'Site Configuration',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PublicHoliday',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                 serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('day', models.PositiveIntegerField()),
                ('month', models.PositiveIntegerField()),
                ('year', models.PositiveIntegerField(null=True, blank=True)),
                ('is_fixed', models.BooleanField(default=True)),
            ],
            options={
                'ordering': (b'is_fixed', b'year', b'month', b'day'),
                'verbose_name': 'Fixed Public Holiday',
                'verbose_name_plural': 'Fixed Public Holidays',
            },
            bases=(models.Model,),
        ),
    ]
