# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bracket', '0005_auto_20150328_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slug',
            name='slug',
            field=models.SlugField(default=b'None'),
            preserve_default=True,
        ),
    ]
