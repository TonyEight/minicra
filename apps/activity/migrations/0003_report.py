# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0002_declaredday'),
        ('business_context', '0003_contract'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                 serialize=False, auto_created=True, primary_key=True)),
                ('off_days', models.FloatField(default=0.0, editable=False)),
                ('days_with_activity',
                 models.FloatField(default=0.0, editable=False)),
                ('month',
                 models.ForeignKey(to='activity.Month', to_field='id')),
                ('contract',
                 models.ForeignKey(
                     to='business_context.Contract', to_field='id')),
            ],
            options={
                'unique_together': set([(b'contract', b'month')]),
                'verbose_name': 'Report',
                'verbose_name_plural': 'Reports',
            },
            bases=(models.Model,),
        ),
    ]
