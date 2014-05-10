# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        (b'context', b'0004_auto_20140508_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name=b'contract',
            name=b'distribution',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name=b'contract',
            name=b'end',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name=b'contract',
            name=b'sold_days',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
    ]
