# Generated by Django 5.0 on 2023-12-22 19:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoapp', '0017_alter_positinline_mypoints'),
    ]

    operations = [
        migrations.AlterField(
            model_name='positinline',
            name='mypoints',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mylines', to='geoapp.worldpoint'),
        ),
    ]