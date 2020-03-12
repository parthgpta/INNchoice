
from django.contrib import admin
from .models import available , timeslots , booked , number

admin.site.register(timeslots)
admin.site.register(available)
admin.site.register(booked)
admin.site.register(number)
