# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        (b'activity', b'0002_offday'),
        (b'context', b'0002_contract'),
    ]

    operations = [
        migrations.CreateModel(
            name=b'Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                (b'month', models.PositiveIntegerField(choices=[(1, b'January'), (2, b'February'), (3, b'March'), (4, b'April'), (5, b'May'), (6, b'June'), (7, b'July'), (8, b'August'), (9, b'September'), (10, b'October'), (11, b'November'), (12, b'December')])),
                (b'year', models.PositiveIntegerField(default=2014)),
                (b'worked_days', models.PositiveIntegerField(default=0, editable=False)),
                (b'off_days', models.PositiveIntegerField(default=0, editable=False)),
                (b'days_with_activity', models.PositiveIntegerField(default=0, editable=False)),
                (b'contract', models.ForeignKey(to=b'context.Contract', to_field='id')),
            ],
            options={
                'unique_together': set([(b'contract', b'month', b'year')]),
                'verbose_name': 'Report',
                'verbose_name_plural': 'Reports',
            },
            bases=(models.Model,),
        ),
    ]
