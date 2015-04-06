# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bracket', '0004_auto_20150328_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='abbrev',
            field=models.ForeignKey(default=0, to='bracket.Nickname'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='nickname',
            name='abbrev',
            field=models.CharField(default=b'None', max_length=25),
            preserve_default=True,
        ),
    ]
