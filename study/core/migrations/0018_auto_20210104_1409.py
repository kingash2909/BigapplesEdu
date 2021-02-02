# Generated by Django 3.0.6 on 2021-01-04 08:39

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20210101_2225'),
    ]

    operations = [
        migrations.AddField(
            model_name='course_details',
            name='platform',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course_details',
            name='price',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course_details',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 4, 14, 9, 38, 257303)),
        ),
    ]