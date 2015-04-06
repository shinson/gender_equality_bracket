# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('region', models.CharField(default=b'WT', max_length=7, choices=[(b'ET', b'East'), (b'WT', b'West'), (b'SH', b'South'), (b'MW', b'Midwest')])),
                ('rank', models.IntegerField(max_length=2)),
                ('magicNo', models.IntegerField(max_length=2)),
                ('female_bb_rate', models.IntegerField(max_length=3)),
                ('male_bb_rate', models.IntegerField(max_length=3)),
                ('female_grad_rate', models.IntegerField(max_length=3)),
                ('male_grad_rate', models.IntegerField(max_length=3)),
                ('female_stem_rate', models.IntegerField(max_length=3)),
                ('male_stem_rate', models.IntegerField(max_length=3)),
                ('female_admin_rate', models.IntegerField(max_length=3)),
                ('male_admin_rate', models.IntegerField(max_length=3)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
