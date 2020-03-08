from django.urls import  path
from . import views

urlpatterns = [
    path('rooms/list' , views.roomlistserializer.as_view(),name= 'list_room'),
    path('timeslots/list' , views.timeslotslistserializer.as_view(),name= 'list_timeslots'),
    path('booked/list/<str:name>', views.bookedlistserializer.as_view(), name='list_booked'),
]