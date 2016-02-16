# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-16 00:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand_type',
            fields=[
                ('BRAND_TYPE_CD', models.IntegerField(primary_key=True, serialize=False)),
                ('BRAND_TYPE_NM', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Brand_owner',
            fields=[
                ('OWNER_CD', models.IntegerField(primary_key=True, serialize=False)),
                ('OWNER_NM', models.CharField(blank=True, max_length=255, null=True)),
                ('OWNER_LINK', models.CharField(blank=True, max_length=255, null=True)),
                ('OWNER_WIKI_EN', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('BSIN', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('BRAND_NM', models.CharField(max_length=255)),
                ('BRAND_TYPE_CD',models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='browser.Brand_type')),
                ('BRAND_LINK', models.CharField(blank=True, max_length=255, null=True)),
                ('OWNER_CD', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='browser.Brand_owner')),
            ],
        ),
        migrations.CreateModel(
            name='Gs1_gcp_rc',
            fields=[
                ('RETURN_CODE', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('RETURN_NAME', models.CharField(max_length=255)),
                ('ORIGIN', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Gs1_gcp',
            fields=[
                ('GCP_CD', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('GLN_CD', models.CharField(max_length=13)),
                ('GLN_NM', models.CharField(max_length=255)),
                ('GLN_ADDR_02', models.CharField(max_length=38)),
                ('GLN_ADDR_03', models.CharField(max_length=38)),
                ('GLN_ADDR_04', models.CharField(max_length=38)),
                ('GLN_ADDR_POSTALCODE', models.CharField(max_length=38)),
                ('GLN_ADDR_CITY', models.CharField(max_length=38)),
                ('GLN_COUNTRY_ISO_CD', models.CharField(max_length=38)),
                ('CONTACT_NAME', models.CharField(max_length=38)),
                ('CONTACT_TEL', models.CharField(max_length=255)),
                ('CONTACT_HOTLINE', models.CharField(blank=True, max_length=255, null=True)),
                ('CONTACT_FAX', models.CharField(max_length=255)),
                ('CONTACT_MAIL', models.CharField(max_length=255)),
                ('CONTACT_WEB', models.CharField(max_length=255)),
                ('GLN_LAST_CHANGE', models.CharField(max_length=10)),
                ('GLN_PROVIDER', models.CharField(max_length=13)),
                ('SEARCH_GTIN_CD', models.CharField(max_length=13)),
                ('GEPIR_GCP_CD', models.CharField(max_length=13)),
                ('ADD_PARTY_ID', models.CharField(max_length=13)),
                ('RETURN_CODE', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='browser.Gs1_gcp_rc')),
                ('SOURCE', models.CharField(max_length=100)),
                ('SYNC_DT', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GS1_gpc',
            fields=[
                ('GPC_LANG', models.CharField(max_length=3)),
                ('GPC_CD', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('GPC_NM', models.TextField()),
                ('GPC_LEVEL', models.CharField(max_length=1)),
                ('SOURCE', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Gtin',
            fields=[
                ('GTIN_CD', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('GTIN_LEVEL_CD', models.IntegerField(blank=True, default=0, null=True)),
                ('GCP_CD', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='browser.Gs1_gcp')),
                ('BSIN',models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='browser.Brand')),
                ('GPC_B_CD',models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='GPC_B_CD', to='browser.GS1_gpc')),
                ('GPC_C_CD',models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='GPC_C_CD', to='browser.GS1_gpc')),
                ('GPC_F_CD',models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='GPC_F_CD', to='browser.GS1_gpc')),
                ('GPC_S_CD',models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='GPC_S_CD', to='browser.GS1_gpc')),
                ('GTIN_NM', models.CharField(blank=True, max_length=255, null=True)),
                ('PRODUCT_LINE', models.CharField(blank=True, max_length=255, null=True)),
                ('M_G', models.FloatField(blank=True, null=True)),
                ('M_OZ', models.FloatField(blank=True, null=True)),
                ('M_ML', models.FloatField(blank=True, null=True)),
                ('M_FLOZ', models.FloatField(blank=True, null=True)),
                ('M_ABV', models.FloatField(blank=True, null=True)),
                ('M_ABW', models.FloatField(blank=True, null=True)),
                ('PKG_UNIT', models.IntegerField(blank=True, default=0, null=True)),
                ('PKG_TYPE_CD', models.IntegerField(blank=True, null=True)),
                ('REF_CD', models.CharField(blank=True, max_length=255, null=True)),
                ('SOURCE', models.CharField(blank=True, max_length=255, null=True)),
                ('IMG', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('GTIN_CD', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('SEARCH_NB', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Nutrition',
            fields=[
                ('GTIN_CD', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='browser.Gtin')),
                ('INGREDIENTS', models.TextField(blank=True, null=True)),
                ('SERV_SIZE_G', models.FloatField(blank=True, null=True)),
                ('SERV_SIZE_ML', models.FloatField(blank=True, null=True)),
                ('SERV_CT', models.FloatField(blank=True, null=True)),
                ('CAL', models.FloatField(blank=True, null=True)),
                ('CAL_FROM_FAT', models.FloatField(blank=True, null=True)),
                ('TOT_FAT_G', models.FloatField(blank=True, null=True)),
                ('TOT_FAT_DV', models.FloatField(blank=True, null=True)),
                ('SAT_FAT_G', models.FloatField(blank=True, null=True)),
                ('SAT_FAT_DV', models.FloatField(blank=True, null=True)),
                ('TRANS_FAT_G', models.FloatField(blank=True, null=True)),
                ('CHOL_MG', models.FloatField(blank=True, null=True)),
                ('CHOL_DV', models.FloatField(blank=True, null=True)),
                ('SOD_MG', models.FloatField(blank=True, null=True)),
                ('SOD_DV', models.FloatField(blank=True, null=True)),
                ('POT_MG', models.FloatField(blank=True, null=True)),
                ('POT_DV', models.FloatField(blank=True, null=True)),
                ('TOT_CARB_G', models.FloatField(blank=True, null=True)),
                ('TOT_CARB_DV', models.FloatField(blank=True, null=True)),
                ('DIET_FIBER_G', models.FloatField(blank=True, null=True)),
                ('DIET_FIBER_DV', models.FloatField(blank=True, null=True)),
                ('SUGARS_G', models.FloatField(blank=True, null=True)),
                ('PROTEIN_G', models.FloatField(blank=True, null=True)),
                ('VITAMIN_A', models.FloatField(blank=True, null=True)),
                ('VITAMIN_C', models.FloatField(blank=True, null=True)),
                ('CALCIUM', models.FloatField(blank=True, null=True)),
                ('IRON', models.FloatField(blank=True, null=True)),
                ('SOURCE', models.TextField(blank=True, null=True)),
                ('SYNC_DT', models.DateField(blank=True, null=True)),
            ],
        ),

    ]
