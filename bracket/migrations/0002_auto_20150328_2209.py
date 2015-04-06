# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bracket', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nickname',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('abbrev', models.CharField(default=b'None', max_length=15)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Slug',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(default=b'None', max_length=25)),
                ('abbrev', models.ForeignKey(to='bracket.Nickname')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TeamStats',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('region', models.CharField(default=b'West', max_length=7, choices=[(b'East', b'East'), (b'West', b'West'), (b'South', b'South'), (b'Midwest', b'Midwest')])),
                ('rank', models.CharField(default=0, max_length=5)),
                ('magic_no', models.CharField(default=0, max_length=5)),
                ('female_bb_rate', models.CharField(default=0, max_length=5)),
                ('male_bb_rate', models.CharField(default=0, max_length=5)),
                ('female_grad_rate', models.CharField(default=0, max_length=5)),
                ('male_grad_rate', models.CharField(default=0, max_length=5)),
                ('female_stem_rate', models.CharField(default=0, max_length=5)),
                ('male_stem_rate', models.CharField(default=0, max_length=5)),
                ('female_admin_rate', models.CharField(default=0, max_length=5)),
                ('male_admin_rate', models.CharField(default=0, max_length=5)),
                ('abbrev', models.ForeignKey(to='bracket.Nickname')),
                ('name', models.ForeignKey(to='bracket.Team')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='team',
            name='female_admin_rate',
        ),
        migrations.RemoveField(
            model_name='team',
            name='female_bb_rate',
        ),
        migrations.RemoveField(
            model_name='team',
            name='female_grad_rate',
        ),
        migrations.RemoveField(
            model_name='team',
            name='female_stem_rate',
        ),
        migrations.RemoveField(
            model_name='team',
            name='magicNo',
        ),
        migrations.RemoveField(
            model_name='team',
            name='male_admin_rate',
        ),
        migrations.RemoveField(
            model_name='team',
            name='male_bb_rate',
        ),
        migrations.RemoveField(
            model_name='team',
            name='male_grad_rate',
        ),
        migrations.RemoveField(
            model_name='team',
            name='male_stem_rate',
        ),
        migrations.RemoveField(
            model_name='team',
            name='rank',
        ),
        migrations.RemoveField(
            model_name='team',
            name='region',
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(default=b'None', max_length=150),
            preserve_default=True,
        ),
    ]
