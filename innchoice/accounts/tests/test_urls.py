from django.test import SimpleTestCase
from accounts.views import *
from django.urls import reverse , resolve
from django.contrib.auth import views as auth_views


class TestUrls(SimpleTestCase):

    def test_home_url_is_resolved(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func.__name__ , auth_views.LoginView.as_view().__name__)
