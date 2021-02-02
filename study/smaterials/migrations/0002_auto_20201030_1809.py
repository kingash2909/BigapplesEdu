# Generated by Django 3.0.6 on 2020-10-30 12:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('smaterials', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='smaterials',
            name='detail',
            field=models.TextField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='smaterials',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='image/'),
            preserve_default=False,
        ),
    ]