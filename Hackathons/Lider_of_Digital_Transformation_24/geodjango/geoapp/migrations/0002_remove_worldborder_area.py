# Generated by Django 3.2.13 on 2023-11-30 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geoapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worldborder',
            name='area',
        ),
    ]