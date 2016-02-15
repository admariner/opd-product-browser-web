# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-12 13:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0018_auto_20160211_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='OWNER_CD',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='browser.BrandOwner'),
        ),
        migrations.AlterField(
            model_name='gtin',
            name='BSIN',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='browser.Brand'),
        ),
        migrations.AlterField(
            model_name='gtin',
            name='GCP_CD',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='browser.GS1gcp'),
        ),
        migrations.AlterField(
            model_name='gtin',
            name='GPC_B_CD',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='GPC_B_CD', to='browser.GS1gpc'),
        ),
        migrations.AlterField(
            model_name='gtin',
            name='GPC_C_CD',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='GPC_C_CD', to='browser.GS1gpc'),
        ),
        migrations.AlterField(
            model_name='gtin',
            name='GPC_F_CD',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='GPC_F_CD', to='browser.GS1gpc'),
        ),
        migrations.AlterField(
            model_name='gtin',
            name='GPC_S_CD',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='GPC_S_CD', to='browser.GS1gpc'),
        ),
        migrations.AlterField(
            model_name='gtin',
            name='GTIN_LEVEL_CD',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='gtin',
            name='IMG',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='gtin',
            name='M_ABV',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='gtin',
            name='M_ABW',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='gtin',
            name='M_FLOZ',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='gtin',
            name='M_G',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='gtin',
            name='M_ML',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='gtin',
            name='M_OZ',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='gtin',
            name='PKG_TYPE_CD',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='gtin',
            name='PKG_UNIT',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
