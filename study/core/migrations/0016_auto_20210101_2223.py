# Generated by Django 3.0.6 on 2021-01-01 16:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20210101_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_details',
            name='updated_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
