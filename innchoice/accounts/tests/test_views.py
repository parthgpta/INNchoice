from django.test import TestCase ,Client
from django.urls import reverse
from accounts.models import person
from bookings.models import  available, number , timeslots
from django.contrib.auth.models import User


class Testviews(TestCase):


    def test_signup_view_get(self):
        self.client = Client()
        response = self.client.get(reverse('signup'))
        self.assertEquals(response.status_code , 200)

    def test_signup_view_post(self):
        self.client = Client()
        response = self.client.post(reverse('signup') )
        self.assertEquals(response.status_code , 200)
        self.assertTemplateUsed(response , 'signup.html')
