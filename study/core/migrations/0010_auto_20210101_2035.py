# Generated by Django 3.0.6 on 2021-01-01 15:05

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20201113_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='course_details',
            name='buttonText',
            field=models.CharField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course_details',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 1, 20, 35, 16, 47219)),
        ),
    ]
