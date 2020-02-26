from django.db import models
# import datetime
from accounts.models import person
from django.contrib.auth.models import User

class Constants:
    room_type =(
        ('Suite' , 'Suite'),
        ('Deluxe' , 'Deluxe'),
        ('Standard' , 'Standard')
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

    # starttime = models.IntegerField()
    # endtime = models.IntegerField()



    def __str__(self):
        return "{}".format(self.manager)

class number(models.Model):
    number = models.IntegerField(default=30)
    day_adv = models.IntegerField(default=5)

    def __str__(self):
        return '{}-{}'.format(self.number,self.day_adv)


# class date(models.Model):
#     day = models.IntegerField()
#     month = models.IntegerField()
#     year = models.IntegerField()
#
#     def __str__(self):
#         return "{}-{}-{}".format(self.day , self.month , self.year)
#
#
# #class Room(models.Model):
# #   manager = models.ForeignKey(person , related_name='manager', on_delete=models.CASCADE)
# #   customer = models.ForeignKey(person ,related_name='customer' ,  on_delete=models.CASCADE)
# #   checkin = models.DateField()
# #   starttime = models.IntegerField(null=True)
# #   endtime = models.IntegerField(null=True)
#
#  #   price  = models.IntegerField()
#
#
# #  def __str__(self):
# #       return "{0}-{1}".format(self.room_type , self.manager)
#
#
# class available(models.Model):
#
#     times =[3,4,5]
#
#     manager = models.ForeignKey(person , on_delete=models.CASCADE)
#     date = models.ManyToManyField(date)
#     available = models.IntegerField(default=30 )
#     starttime = models.IntegerField(null=True)
#     endtime = models.IntegerField(null=True)
#     room_type =models.CharField(choices=Constants.room_type , max_length=8 , default='Suite')
#
#     def __str__(self):
#         return "{}-av".format(self.manager)
#
