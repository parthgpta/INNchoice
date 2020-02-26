import datetime
from .models import available , timeslots ,number
from django.shortcuts import render , redirect , get_object_or_404
from .forms import edittime
from accounts.models import person

def homepage(request):

    a  = datetime.date.today()
    t  = timeslots.objects.all()
    if number.objects.all():
        num = number.objects.all()
    else:
        num = number()
        num.save()
    d = a.day
    m = a.month
    print(num)
    adv = num[0].day_adv

    for i in range(adv+1):
        for j in t:
            if not available.objects.filter(day = d+i, starttime = j.starttime,month=m):
                z = available(day = d+i , month = m , year = 2020 ,room_type = 'Suite' , manager = request.user.person ,number = num[0].number,
                starttime= j.starttime , endtime = j.endtime)
                z.save()

    a = available.objects.filter(day__gte = d , month__gte = m)



#     a = datetime.date.today()
#     if request.user.person.user_type == 'Room Manager':
#         z = available( manager=request.user.person)
#         l = z.times
#         print(l)
#         for i in range(0, 10):
#             for j in l:
#                 print(j)
#                 if not available.objects.filter(date="{}-{}-{}".format(2020, 2, a.day+i) , starttime = j):
#
#                     print("YES")
#
#                     a = available(date="{}-{}-{}".format(2020, 2, 15 + i), room_type='Suite', available=30,
#                               starttime = j,manager=request.user.person)
#                     a.save()
#     #available.objects.filter(date = "2020-02-21").delete()
#    # available.objects.filter(date="{}-{}-{}".format(2020, 2, 15)).update(available = 17)
#    # z =available.objects.filter(date="{}-{}-{}".format(2020, a.month, a.day+3))
#    # print(z[0].times[0])
#
#     av = available.objects.all()
    return render(request , 'home.html' ,{'av':a} )


def addtime(request):
    if request.user.person.user_type == 'Room Manager':
        if request.method == 'POST':
            st = request.POST['starttime']
            et = request.POST['endtime']
            z  = timeslots(starttime = st , endtime= et)
            z.save()
            return redirect('home')
        return render(request , 'changetime.html' , {})
    else:
        return redirect('home')



def profile(request):
    if request.user.person.user_type == 'Room Manager':
        ts = timeslots.objects.all()
        return render(request , 'profile.html' , {'ts':ts})

    else:
        return render(request , 'profile.html', {})

def deltime(request , pk):
    time = get_object_or_404(timeslots , pk=pk)
    time.delete()
    return  redirect('profile')

def edittime(request , pk):
    time = timeslots.objects.filter(pk=pk)
    print(time)
    if request.method == 'POST':
        form = edittime(request.POST , instance=time)
        if form.is_valid():
            time = form.save()
            return redirect('profile')
    else:
        form = edittime(instance=time)

    return render(request , 'edittime.html' , {'form':form})


def days_adv(request):
    if request.user.person.user_type == 'Room Manager':
        if request.method == 'POST':
            num = request.POST['number']
            days = request.POST['days']
            #request.user.person.update(days_adv = days)

            number.objects.filter(id=1).update(day_adv = days)
            number.objects.filter(id = 1).update(number = num)
            #a[0].update(number  =num)
            return redirect('home')
        return render(request , 'number.html' , {})
    else:
        return redirect('home')

def check(request):
    return render(request , 'base2.html')
