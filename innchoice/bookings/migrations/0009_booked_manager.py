# Generated by Django 3.0.2 on 2020-03-05 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0008_booked'),
    ]

    operations = [
        migrations.AddField(
            model_name='booked',
            name='manager',
            field=models.CharField(default='rahul', max_length=20),
            preserve_default=False,
        ),
    ]