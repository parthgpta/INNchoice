from django.test import TestCase
from innchoice.bookings.models import available , booked

class bookedemodeltest(TestCase):

    def setup(cls):
      booked.objects.create(date = 10,month=2,year=2020,room_t ='Suite',starttime=7,endtime=12,manager='tester',customer='user')

    def room_t_name_label(self):
        author = booked.objects.get(id=1)
        field_label = author._meta.get_field('room_t').verbose_name
        self.assertEquals(field_label, 'room t')

    def test_object_name_is_last_name_comma_first_name(self):
        author = booked.objects.get(id=1)
        expected_object_name = '{}-{}'.format(self.customer , self.date)
        self.assertEquals(expected_object_name, str(author))
