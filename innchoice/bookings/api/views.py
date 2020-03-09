from rest_framework.generics import ListAPIView ,CreateAPIView
from bookings.models import available , booked, timeslots
from .serializers import roomlistserializer ,timeslotslistserializer ,bookedlistserializer

class roomlistserializer(ListAPIView):
    queryset = available.objects.all()
    serializer_class = roomlistserializer

class timeslotslistserializer(ListAPIView):
    queryset = timeslots.objects.all()
    serializer_class = timeslotslistserializer

class bookedlistserializer(ListAPIView):
    queryset = booked.objects.filter(customer = 'abhi bonga')
    serializer_class = bookedlistserializer


