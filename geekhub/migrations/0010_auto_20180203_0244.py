# Generated by Django 2.0.1 on 2018-02-03 00:44

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geekhub', '0009_auto_20180203_0237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='requirements',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), blank=True, size=None),
        ),
    ]
