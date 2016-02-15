# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-04 06:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0012_auto_20160204_1332'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrandOwner',
            fields=[
                ('OWNER_CD', models.IntegerField(primary_key=True, serialize=False)),
                ('OWNER_NM', models.CharField(blank=True, max_length=255, null=True)),
                ('OWNER_LINK', models.CharField(blank=True, max_length=255, null=True)),
                ('OWNER_WIKI_EN', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
