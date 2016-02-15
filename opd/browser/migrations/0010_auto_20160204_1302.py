# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-04 05:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0009_auto_20160204_1237'),
    ]

    operations = [
        migrations.CreateModel(
            name='GS1gpc',
            fields=[
                ('GPC_LANG', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('GPC_CD', models.CharField(max_length=20)),
                ('GPC_NM', models.TextField()),
                ('GPC_LEVEL', models.CharField(max_length=1)),
                ('SOURCE', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='gs1gpc',
            unique_together=set([('GPC_LANG', 'GPC_CD')]),
        ),
    ]
