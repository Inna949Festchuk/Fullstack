# Generated by Django 5.0 on 2023-12-29 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geoapp', '0027_alter_worldline_options_alter_worldpoint_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='worldline',
            options={'verbose_name_plural': 'Схема движеия по азимутам'},
        ),
        migrations.AlterModelOptions(
            name='worldpoint',
            options={'verbose_name_plural': 'Схема расположения ориентиров'},
        ),
    ]