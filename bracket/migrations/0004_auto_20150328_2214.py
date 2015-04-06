# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bracket', '0003_auto_20150328_2210'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamStat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('region', models.CharField(default=b'West', max_length=7, choices=[(b'East', b'East'), (b'West', b'West'), (b'South', b'South'), (b'Midwest', b'Midwest')])),
                ('rank', models.CharField(max_length=5)),
                ('magic_no', models.CharField(max_length=5)),
                ('female_bb_rate', models.CharField(max_length=5)),
                ('male_bb_rate', models.CharField(max_length=5)),
                ('female_grad_rate', models.CharField(max_length=5)),
                ('male_grad_rate', models.CharField(max_length=5)),
                ('female_stem_rate', models.CharField(max_length=5)),
                ('male_stem_rate', models.CharField(max_length=5)),
                ('female_admin_rate', models.CharField(max_length=5)),
                ('male_admin_rate', models.CharField(max_length=5)),
                ('abbrev', models.ForeignKey(to='bracket.Nickname')),
                ('name', models.ForeignKey(to='bracket.Team')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='teamstats',
            name='abbrev',
        ),
        migrations.RemoveField(
            model_name='teamstats',
            name='name',
        ),
        migrations.DeleteModel(
            name='TeamStats',
        ),
    ]
