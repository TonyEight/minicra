# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business_context', '0003_contract'),
        ('activity', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeclaredDay',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('period', models.PositiveIntegerField(default=1, choices=[(1, b'Morning'), (2, b'Afternoon'), (3, b'Whole day')])),
                ('type', models.PositiveIntegerField(default=3, choices=[(1, b'Activity'), (2, b'Off Day')])),
                ('contract', models.ForeignKey(to='business_context.Contract', to_field='id')),
                ('comment', models.TextField(blank=True)),
            ],
            options={
                'ordering': (b'date', b'contract'),
                'verbose_name': 'Activity',
                'verbose_name_plural': 'Activities',
            },
            bases=(models.Model,),
        ),
    ]
