from django.db import models
# import datetime
from accounts.models import person
from django.contrib.auth.models import User

class Constants:
    room_type =(
        ('Suite' , 'Suite'),
        ('Deluxe' , 'Deluxe'),
    )


class timeslots(models.Model):
    starttime = models.IntegerField()
    endtime = models.IntegerField()

    def __str__(self):
        return "{}-{}".format(self.starttime, self.endtime)


class available(models.Model):
    manager = models.ForeignKey(person , on_delete=models.CASCADE)
    number = models.IntegerField(default=30)
    day = models.IntegerField()
    month = models.IntegerField()
    year = models.IntegerField()
    room_type = models.CharField(max_length= 10 , default='Suite' , choices= Constants.room_type)
    starttime = models.IntegerField()
    endtime = models.IntegerField()

    def __str__(self):
        return "{}".format(self.manager)

class number(models.Model):
    number = models.IntegerField(default=30)
    day_adv = models.IntegerField(default=5)

    def __str__(self):
        return '{}-{}'.format(self.number,self.day_adv)

