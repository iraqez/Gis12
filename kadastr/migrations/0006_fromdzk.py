# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-25 07:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kadastr', '0005_przem_type_dzk'),
    ]

    operations = [
        migrations.CreateModel(
            name='fromDzk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cadnum', models.CharField(max_length=22)),
                ('koatuu', models.CharField(max_length=10)),
                ('zona', models.CharField(max_length=2)),
                ('kvartal', models.CharField(max_length=3)),
                ('parcel', models.CharField(max_length=4)),
                ('purpose', models.CharField(max_length=30)),
                ('unit_area', models.CharField(max_length=25)),
                ('area', models.FloatField()),
                ('ownershipcode', models.CharField(max_length=5)),
                ('id_office', models.CharField(max_length=5)),
                ('st_xmax', models.FloatField()),
                ('st_ymax', models.FloatField()),
                ('st_xmin', models.FloatField()),
                ('st_ymin', models.FloatField()),
            ],
        ),
    ]