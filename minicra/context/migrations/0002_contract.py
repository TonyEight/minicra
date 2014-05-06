# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        (b'context', b'0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name=b'Contract',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                (b'mission', models.CharField(max_length=260)),
                (b'description', models.TextField(blank=True)),
                (b'project', models.ForeignKey(to=b'context.Project', to_field='id')),
                (b'client', models.ForeignKey(to=b'context.Client', to_field='id')),
                (b'actor', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id')),
                (b'start', models.DateField()),
                (b'end', models.DateField(blank=True)),
                (b'sold_days', models.PositiveIntegerField(blank=True)),
                (b'distribution', models.PositiveIntegerField(blank=True)),
            ],
            options={
                'verbose_name': 'Contract',
                'verbose_name_plural': 'Contracts',
            },
            bases=(models.Model,),
        ),
    ]
