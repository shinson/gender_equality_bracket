# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bracket', '0006_auto_20150328_2314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slug',
            name='abbrev',
        ),
        migrations.AddField(
            model_name='slug',
            name='slugName',
            field=models.CharField(default=b'None', max_length=25),
            preserve_default=True,
        ),
    ]
