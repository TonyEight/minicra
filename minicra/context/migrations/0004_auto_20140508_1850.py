# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        (b'context', b'0003_auto_20140508_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name=b'client',
            name=b'service',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
