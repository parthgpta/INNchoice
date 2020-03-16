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
        time_s = timeslots(starttime=12 , endtime=5)
        time_s.save()
        num.save()

    if timeslots.objects.all():
        pass
    else:
        time_s = timeslots(starttime=12, endtime=5)
        time_s.save()


    d = a.day
    m = a.month
    num = number.objects.all()
    print(num[0])
    print()


    y = a.year
    if y%4==0:
        month_d[1] = 29

    mon = m
    monn = m
    days_num = month_d[m-1]

    print(num)
    num = number.objects.all()
    adv = num[0].day_adv
    room =['Suite'  , 'Deluxe' ]
    
    if request.user.person.user_type == 'Room Manager':
        for i in range(adv+1):
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

    a = available.objects.filter( day__gte = d , number__gt =0 ).order_by('day','starttime')
    b = available.objects.filter(month__gt = mon , number__gt = 0).order_by('day','starttime')
    time = timeslots.objects.all()
    return render(request , 'home.html' ,{'av':a ,'year':y ,'b':b ,'timeslots':time} )


def profile(request):
    return render(request , 'profile.html', {})

def deltime(request , pk):
    time = get_object_or_404(timeslots , pk=pk)
    time.delete()
    return  redirect('time_slots')

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


def time_slots(request):
    if request.user.person.user_type == 'Room Manager':
        num = number.objects.all()
        adv = num[0].day_adv
        room = num[0].number
        ts = timeslots.objects.all()       
        if request.method == 'POST':
            num = request.POST['number']
            days = request.POST['days']
            st = request.POST['starttime']
            et = request.POST['endtime']
            et = str(et)
            st = str(st)
            if(st!="" and et!=""):
                z  = timeslots(starttime = st , endtime= et)
                z.save()
            num = str(num)
            if(num!=""):
                number.objects.filter(id = 1).update(number = num)
            days = str(days)
            if(days!=""):
                number.objects.filter(id=1).update(day_adv = days)
            
            return redirect('time_slots')
        return render(request , 'number.html' , {'ts':ts ,'adv':adv,'room':room})
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
        a = booked.objects.filter(customer = name).order_by('date','startime')

    else:
        a = booked.objects.all().order_by('date')
    return render(request, 'booked.html' , {'booked':a})

def delbook(request ,pk):
    b = booked.objects.filter(id = pk)
    m = available.objects.filter(day = b[0].date , month = b[0].month , year = b[0].year ,
                                 starttime = b[0].startime , endtime = b[0].endtime)
    if m:
        num = m[0].number
        m = available.objects.filter(day=b[0].date, month=b[0].month, year=b[0].year,
                                 starttime=b[0].startime, endtime=b[0].endtime).update(number = num+1)
    b.delete()
    return redirect('profile')

def available_room(request,pk):
    room = available.objects.filter(id = pk)
    if room:
        print(pk)
    room.delete()
    room = available.objects.filter(id=pk)


    print('d')
    return redirect('home')

def add_specific(request):
    if request.user.person.user_type == 'Room Manager':
        if request.method == 'POST':
            date = request.POST['date']
            date = str(date)
            if date!="":
                p  = date.split('-')
                if len(p) != 3:
                    return redirect('add_specific')
                day = p[0]
                month = p[1]
                year = p[2]
            time = request.POST['time']
            time = str(time)
            if time!="":
                t = time.split("-")

                if len(t)!=2:
                    return redirect('add_specific')
                st = t[0]
                et = t[1]

            ty = request.POST['type']
            ty = str(ty)
            num = number.objects.all()
            num = num[0].number
            if ty!="" and date!="" and time!="":
                z = available(day = day, month = month , year = year ,room_type =ty , manager = request.user.person ,
                        starttime= st , endtime = et , number= num)
                z.save()
                return redirect('home')
            else:
                return render(request, 'add_room.html')

        else:
            return render(request , 'add_room.html')
    else:
        return redirect('home')

@login_required(login_url='login')
def api_info(request):
    return render(request , 'api_info.html')
