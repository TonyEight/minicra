# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        (b'context', b'0002_contract'),
        (b'activity', b'0003_offday'),
    ]

    operations = [
        migrations.CreateModel(
            name=b'Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                (b'off_days', models.FloatField(default=0.0, editable=False)),
                (b'days_with_activity', models.FloatField(default=0.0, editable=False)),
                (b'month', models.ForeignKey(to=b'activity.Month', to_field='id')),
                (b'contract', models.ForeignKey(to=b'context.Contract', to_field='id')),
            ],
            options={
                'unique_together': set([(b'contract', b'month')]),
                'verbose_name': 'Report',
                'verbose_name_plural': 'Reports',
            },
            bases=(models.Model,),
        ),
    ]
