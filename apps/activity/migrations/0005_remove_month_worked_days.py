# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0004_report_excel_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='month',
            name='worked_days',
        ),
    ]
