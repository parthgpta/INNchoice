
from django.contrib import admin
from .models import available , timeslots

admin.site.register(timeslots)
admin.site.register(available)