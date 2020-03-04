# Generated by Django 3.0.2 on 2020-02-09 05:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0010_auto_20200209_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='checkin',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='checkout',
            field=models.DateField(auto_now_add=True, default=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='room_type',
            field=models.CharField(choices=[('Suite', 'Suite'), ('Deluxe', 'Deluxe'), ('Standard', 'Standard')], default='Suite', max_length=8),
        ),
    ]