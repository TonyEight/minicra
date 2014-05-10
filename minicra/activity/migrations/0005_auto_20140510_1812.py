# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0004_report'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='period',
            field=models.PositiveIntegerField(default=3, choices=[(1, b'Morning'), (2, b'Afternoon'), (3, b'Whole day')]),
        ),
    ]
