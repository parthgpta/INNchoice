import datetime
from .models import available , timeslots ,number
from django.shortcuts import render , redirect , get_object_or_404
from .forms import edittime
from accounts.models import person
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def homepage(request):
    month_n =['January','February' , 'March','April','May','June','July','August','September','October','November','December']
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
    print(num)
    adv = num[0].day_adv
    room =['Suite'  , 'Deluxe' ]
    
    if request.user.person.user_type == 'Room Manager':
        for i in range(adv+1):
            for j in t:
                for k in room:
                    if not available.objects.filter(day = d+i, starttime = j.starttime,month=m,room_type = k):
                        z = available(day = d+i , month = m , year = 2020 ,room_type =k , manager = request.user.person ,number = num[0].number,
                        starttime= j.starttime , endtime = j.endtime )
                        z.save()

    a = available.objects.filter(day__gte = d , month__gte = m)
    return render(request , 'home.html' ,{'av':a ,'month':month_n[m-1] ,'year':y} )


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
        return redirect('home')


    return render(request , 'book_room.html' ,{'room':room})

    
