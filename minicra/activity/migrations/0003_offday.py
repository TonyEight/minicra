# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        (b'activity', b'0002_activity'),
        (b'context', b'0002_contract'),
    ]

    operations = [
        migrations.CreateModel(
            name=b'OffDay',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                (b'date', models.DateField()),
                (b'period', models.PositiveIntegerField(default=3, choices=[(1, b'morning'), (2, b'afternoon'), (3, b'all_day')])),
                (b'contract', models.ForeignKey(to=b'context.Contract', to_field='id')),
                (b'comment', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Off Day',
                'verbose_name_plural': 'Off Days',
            },
            bases=(models.Model,),
        ),
    ]
