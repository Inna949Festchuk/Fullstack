# Generated by Django 5.0 on 2023-12-27 01:23

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geoapp', '0022_remove_worldpoint_myline_pointinline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worldline',
            name='location',
            field=django.contrib.gis.db.models.fields.LineStringField(srid=28404),
        ),
        migrations.AlterField(
            model_name='worldpoint',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(srid=28404),
        ),
    ]