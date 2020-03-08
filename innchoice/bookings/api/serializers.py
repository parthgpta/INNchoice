from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from rest_framework import serializers
from bookings.models import timeslots  ,available , booked

class roomlistserializer(ModelSerializer):
    class Meta:
        model = available
        fields = [
            'number',
            'day',
            'month',
            'year',
            'room_type',
            'starttime',
            'endtime' ,
        ]

class timeslotslistserializer(ModelSerializer):
    class Meta:
        model = available
        fields = [
            'starttime',
            'endtime',
        ]

class bookedlistserializer(ModelSerializer):
    class Meta:
        model = booked
        fields = [
            'customer',
            'manager',
            'date',
            'month',
            'year',
            'room_t',
            'startime',
            'endtime' ,
        ]
