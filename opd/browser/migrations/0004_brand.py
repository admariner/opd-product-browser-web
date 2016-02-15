# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-04 02:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0003_auto_20160203_1844'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('BSIN', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('BRAND_NM', models.CharField(max_length=255)),
                ('BRAND_TYPE_CD', models.IntegerField(default=0)),
                ('BRAND_LINK', models.CharField(max_length=255)),
            ],
        ),
    ]
