import datetime
from .models import available , timeslots ,number , booked
from django.shortcuts import render , redirect , get_object_or_404
from .forms import edittime
from accounts.models import person
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def homepage(request):
    month_n =['January','February' , 'March','April','May','June','July','August','September','October','November','December']
    month_d = [31,28,31,30,31,30,31,31,30,31,30,31]
    a  = datetime.date.today()
    t  = timeslots.objects.all()
    if number.objects.all():
        num = number.objects.all()
    else:
        num = number()
        num.save()
    d = a.day
    m = a.month

    y = a.year
    if y%4==0:
        month_d[1] = 29
    m = 6
    mon = m
    monn = m
    days_num = month_d[m-1]
    d =  26

    print(num)
    adv = num[0].day_adv
    room =['Suite'  , 'Deluxe' ]
    
    if request.user.person.user_type == 'Room Manager':
        for i in range(adv+8):
            for j in t:
                for k in room:
                    z = d+i
                    if z>days_num:
                        z = z%days_num
                        m = monn +1
                    if not available.objects.filter(day = z, starttime = j.starttime,month=m,room_type = k):
                        z = available(day = z , month = m , year = 2020 ,room_type =k , manager = request.user.person ,number = num[0].number,
                        starttime= j.starttime , endtime = j.endtime )
                        z.save()

    a = available.objects.filter( day__gte = d , number__gt =0)
    b = available.objects.filter(month__gt = mon , number__gt = 0)
    return render(request , 'home.html' ,{'av':a ,'year':y ,'b':b} )


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
            number.objects.filter(id=1).update(day_adv = days)
            number.objects.filter(id = 1).update(number = num)
            return redirect('home')
        return render(request , 'number.html' , {})
    else:
        return redirect('home')

def check(request):
    av = available.objects.all()
    return render(request , 'base2.html',{'av':av})


def book_room(request , pk):
    room = available.objects.get(id=pk)
    if request.method =='POST':
        a= available.objects.filter(id=pk)
        print(a[0].number)
        a = a[0].number
        available.objects.filter(id=pk).update(number = a-1)
        z = booked(date= room.day , month = room.month , year = room.year , room_t = room.room_type,
                   startime =room.starttime,endtime= room.endtime , customer = request.user.person.name ,manager = room.manager)
        z.save()
        return redirect('home')


    return render(request , 'book_room.html' ,{'room':room})

    
def booked_room(request ,name):
    if request.user.person.user_type == 'Customer':
        a = booked.objects.filter(customer = name)
    else:
        a = booked.objects.all()
    return render(request, 'booked.html' , {'booked':a})

def delbook(request ,pk):
    b = booked.objects.filter(id = pk)
    m = available.objects.filter(day = b[0].date , month = b[0].month , year = b[0].year ,
                                 starttime = b[0].startime , endtime = b[0].endtime)
    num = m[0].number
    m = available.objects.filter(day=b[0].date, month=b[0].month, year=b[0].year,
                                 starttime=b[0].startime, endtime=b[0].endtime).update(number = num+1)
    b.delete()
    return redirect('profile')