# Generated by Django 3.0.2 on 2020-02-09 05:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0008_auto_20200209_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='checkin',
            field=models.DateField(default=datetime.date(1970, 1, 1)),
        ),
    ]
