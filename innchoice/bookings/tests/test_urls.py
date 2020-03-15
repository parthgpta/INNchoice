from django.test import SimpleTestCase
from bookings.views import *
from django.urls import reverse , resolve


class TestUrls(SimpleTestCase):

    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func , homepage)

    def test_profile_url_is_resolved(self):
        url = reverse('profile')
        self.assertEquals(resolve(url).func , profile)

    def test_api_url_is_resolved(self):
        url = reverse('api_info')
        self.assertEquals(resolve(url).func ,api_info)

    def test_book_room_url_is_resolved(self):
        url = reverse('book_room' ,args=[45])
        self.assertEquals(resolve(url).func ,book_room)

    def test_booked_room_url_is_resolved(self):
        url = reverse('booked_details' ,args=['xyz'])
        self.assertEquals(resolve(url).func ,booked_room)
