from django.db import models
from accounts.models import person
from django.contrib.auth.models import User

class Constants:
    room_type =(
        ('Suite' , 'Suite'),
        ('Deluxe' , 'Deluxe'),
        ('Standard' , 'Standard')
    )


class Room(models.Model):
    manager = models.ForeignKey(person , related_name='manager', on_delete=models.CASCADE)
    customer = models.ForeignKey(person ,related_name='customer' ,  on_delete=models.CASCADE)
    checkin = models.DateField()
    room_type =models.CharField(choices=Constants.room_type , max_length=8 , default='Suite')
    price  = models.IntegerField()
    checkout = models.DateField()

    def __str__(self):
        return "{0}-{1}".format(self.room_type , self.manager)
