# Generated by Django 3.2.9 on 2021-11-19 17:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20211119_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='when',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
