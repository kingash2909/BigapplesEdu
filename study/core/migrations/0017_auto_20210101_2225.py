# Generated by Django 3.0.6 on 2021-01-01 16:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20210101_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_details',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 1, 22, 25, 7, 738281)),
        ),
    ]