# Generated by Django 3.0.2 on 2020-02-09 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0004_auto_20200209_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='end_time',
            field=models.TimeField(default=10),
        ),
    ]
