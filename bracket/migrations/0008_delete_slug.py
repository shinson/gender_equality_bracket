# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bracket', '0007_auto_20150329_0022'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Slug',
        ),
    ]
