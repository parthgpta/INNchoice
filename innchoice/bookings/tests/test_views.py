from django.test import TestCase ,Client
from django.urls import reverse
from accounts.models import person
from bookings.models import  available, number , timeslots
from django.contrib.auth.models import User


class Testviews(TestCase):


    def test_profile_view(self):
        self.client = Client()
        response = self.client.get(reverse('profile'))
        self.assertEquals(response.status_code , 200)
        self.assertTemplateUsed(response , 'profile.html')

    def test_home_login_required_view(self):
        self.client = Client()
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code , 302)  #Redirects to Login Page


    def test_home_view(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='test', email='test@g.com',
            password='test')

        person.objects.create(
            user=self.user,
            name='test',
            gender='Male',
            dob='1975-10-10',
            phone='955955659',
            user_type='Room Manager'
        )

        self.client.login(username="test", password="test")
        response = self.client.post(reverse('home'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response , 'home.html')


    def test_book_room_view_get(self):
        self.client = Client()

        self.user = User.objects.create_user(
            username='test', email='test@g.com',
            password='test')

        person.objects.create(
            user=self.user,
            name='test',
            gender='Male',
            dob='1975-10-10',
            phone='955955659',
            user_type='Room Manager'
        )
        available.objects.create(
            day=10, month=6, year=2020, room_type='Suite', manager=self.user.person, number=30,
            starttime=7, endtime=12
        )

        response  = self.client.get(reverse('book_room' , args=[1]))
        self.assertEquals(response.status_code , 200)
        self.assertTemplateUsed(response , 'book_room.html')


    def test_book_room__view_post(self):
        self.client = Client()

        self.user = User.objects.create_user(
            username='test', email='test@g.com',
            password='test')

        person.objects.create(
            user=self.user,
            name='test',
            gender='Male',
            dob='1975-10-10',
            phone='955955659',
            user_type='Customer'
        )
        available.objects.create(
            day=10, month=6, year=2020, room_type='Suite', manager=self.user.person, number=30,
            starttime=7, endtime=12
        )
        self.client.login(username="test", password="test")
        response  = self.client.post(reverse('book_room' , args=[1]))

        self.assertEquals(response.status_code , 302)



    def test_timeslots_customer_view(self):

        self.client = Client()

        self.user = User.objects.create_user(
            username='test', email='test@g.com',
            password='test')
        person.objects.create(
            user=self.user,
            name='test',
            gender='Male',
            dob='1975-10-10',
            phone='955955659',
            user_type='Customer'
        )
        self.client.login(username="test", password="test")
        response = self.client.get(reverse('time_slots'))
        self.assertEquals(response.status_code, 302)

    def test_timeslots_manager_get_view(self):
        self.client = Client()
        self.client = Client()

        self.user = User.objects.create_user(
            username='test', email='test@g.com',
            password='test')
        person.objects.create(
            user=self.user,
            name='test',
            gender='Male',
            dob='1975-10-10',
            phone='955955659',
            user_type='Room Manager'
        )
        number.objects.create(
            number= 30,
            day_adv = 6
        )
        self.client.login(username="test", password="test")
        response = self.client.get(reverse('time_slots'))
        self.assertEquals(response.status_code, 200)

    def test_timeslots_manager_post_view(self):
        self.client = Client()
        self.client = Client()

        self.user = User.objects.create_user(
            username='test', email='test@g.com',
            password='test')
        person.objects.create(
            user=self.user,
            name='test',
            gender='Male',
            dob='1975-10-10',
            phone='955955659',
            user_type='Room Manager'
        )
        number.objects.create(
            number= 30,
            day_adv = 6
        )
        timeslots.objects.create(
            starttime = 7,
            endtime = 12

        )
        self.client.login(username="test", password="test")
        response = self.client.post(reverse('time_slots') , {
            'number' : 45,
            'days' : 5 ,
            'starttime' : 7,
            'endtime' : 12

        })
        self.assertEquals(response.status_code, 302)


    def test_add_specific_view_customer(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='test', email='test@g.com',
            password='test')
        person.objects.create(
            user=self.user,
            name='test',
            gender='Male',
            dob='1975-10-10',
            phone='955955659',
            user_type='Customer'
        )
        self.client.login(username="test", password="test")
        response = self.client.get(reverse('add_specific'))
        self.assertEquals(response.status_code, 302)

    def test_add_specific_view_manager_get(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='test', email='test@g.com',
            password='test')
        person.objects.create(
            user=self.user,
            name='test',
            gender='Male',
            dob='1975-10-10',
            phone='955955659',
            user_type='Room Manager'
        )
        self.client.login(username="test", password="test")
        response = self.client.get(reverse('add_specific'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response , 'add_room.html')


    def test_add_specific_view_manager_post_data_not_all(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='test', email='test@g.com',
            password='test')
        person.objects.create(
            user=self.user,
            name='test',
            gender='Male',
            dob='1975-10-10',
            phone='955955659',
            user_type='Room Manager'
        )
        number.objects.create(
            number=30,
            day_adv=6
        )
        self.client.login(username="test", password="test")
        response = self.client.post(reverse('add_specific'),{               #All iformation  NOT provided here
            'date': '10-3-2020',
            'time' : '7-12',
            'type' :''

        })
        self.assertEquals(response.status_code, 200)                        #Renders 'add_room.html' http_response = 200
        self.assertTemplateUsed(response , 'add_room.html')

    def test_add_specific_view_manager_post_data_all(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='test', email='test@g.com',
            password='test')
        person.objects.create(
            user=self.user,
            name='test',
            gender='Male',
            dob='1975-10-10',
            phone='955955659',
            user_type='Room Manager'
        )
        number.objects.create(
            number=30,
            day_adv=6
        )
        self.client.login(username="test", password="test")
        response = self.client.post(reverse('add_specific'),{               #All iformation provided here
            'date': '10-3-2020',
            'time' : '7-12',
            'type' :'Suite'

        })
        self.assertEquals(response.status_code, 302)                        #redirects home , http_response = 302
