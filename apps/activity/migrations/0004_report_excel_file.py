# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0003_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='excel_file',
            field=models.FileField(upload_to=b'', null=True, editable=False),
            preserve_default=True,
        ),
    ]
