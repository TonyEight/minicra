# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('business_context', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('service', models.CharField(max_length=200, null=True, blank=True)),
                ('organisation', models.ForeignKey(to='business_context.Organisation', to_field='id')),
                ('actor', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id')),
            ],
            options={
                'unique_together': set([(b'name', b'actor')]),
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
            },
            bases=(models.Model,),
        ),
    ]
