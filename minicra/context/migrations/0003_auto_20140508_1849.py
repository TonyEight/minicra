# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        (b'context', b'0002_contract'),
    ]

    operations = [
        migrations.AlterField(
            model_name=b'contract',
            name=b'project',
            field=models.ForeignKey(to_field='id', blank=True, to=b'context.Project', null=True),
        ),
    ]
