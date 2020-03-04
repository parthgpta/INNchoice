import datetime
from django.db import models
from django.contrib.auth.models import  User
from django.utils import timezone

class CONSTANTS:
    gender = (
        ('Male' , 'Male'),
        ('Female', 'Female'),
        ('Others' , 'Others'),
    )

    user_type = (
        ('Room Manager' , 'Room Manager'),
        ('Customer' , 'Customer'),
    )

class person(models.Model):
    user = models.OneToOneField(User ,on_delete=models.CASCADE )
    name = models.CharField(max_length=20 , blank=False )
    gender = models.CharField(choices= CONSTANTS.gender , default='Male' ,max_length=8)
    dob = models.DateField( default =datetime.date(1970, 1, 1))
    phone = models.BigIntegerField(null= False , default=999999999)
    user_type = models.CharField(choices=CONSTANTS.user_type , max_length= 20 ,blank=False,default='Customer')

    @property
    def age(self):
        timedelta = timezone.now().date() - self.dob
        return int(timedelta.days / 365)

    def __str__(self):
        return "{0}".format(self.name )


