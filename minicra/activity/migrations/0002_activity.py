# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        (b'context', b'0002_contract'),
        (b'activity', b'0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name=b'Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                (b'date', models.DateField()),
                (b'period', models.PositiveIntegerField(default=3, choices=[(1, b'morning'), (2, b'afternoon'), (3, b'whole day')])),
                (b'contract', models.ForeignKey(to=b'context.Contract', to_field='id')),
                (b'comment', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Activity',
                'verbose_name_plural': 'Activities',
            },
            bases=(models.Model,),
        ),
    ]
