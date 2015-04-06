# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bracket', '0002_auto_20150328_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamstats',
            name='female_admin_rate',
            field=models.CharField(max_length=5),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teamstats',
            name='female_bb_rate',
            field=models.CharField(max_length=5),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teamstats',
            name='female_grad_rate',
            field=models.CharField(max_length=5),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teamstats',
            name='female_stem_rate',
            field=models.CharField(max_length=5),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teamstats',
            name='magic_no',
            field=models.CharField(max_length=5),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teamstats',
            name='male_admin_rate',
            field=models.CharField(max_length=5),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teamstats',
            name='male_bb_rate',
            field=models.CharField(max_length=5),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teamstats',
            name='male_grad_rate',
            field=models.CharField(max_length=5),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teamstats',
            name='male_stem_rate',
            field=models.CharField(max_length=5),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teamstats',
            name='rank',
            field=models.CharField(max_length=5),
            preserve_default=True,
        ),
    ]
