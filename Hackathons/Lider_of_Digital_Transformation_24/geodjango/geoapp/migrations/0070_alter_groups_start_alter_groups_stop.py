# Generated by Django 4.0.3 on 2024-06-19 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoapp', '0069_alter_groups_stop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groups',
            name='start',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='groups',
            name='stop',
            field=models.DateTimeField(auto_now=True),
        ),
    ]