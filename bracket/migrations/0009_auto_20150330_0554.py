# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bracket', '0008_delete_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamstat',
            name='magic_no',
            field=models.FloatField(max_length=5),
            preserve_default=True,
        ),
    ]
