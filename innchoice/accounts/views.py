from django.shortcuts import render , redirect
from .forms import Userprofile , Userform
from django.contrib.auth import  authenticate,login

# Create your views here.

def redir(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return redirect('login')


def signup(request):

    if request.method == 'POST':
        userprofile = Userprofile(data=request.POST)
        userform = Userform(data = request.POST)
        if userform.is_valid() and userprofile.is_valid():
            user = userform.save()
            user.set_password(user.password)
            user.save()
            profile = userprofile.save(commit = False)
            profile.user = user
            profile.save()
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username = username , password = password)
            if user:
                login(request,user)
            return redirect('home')
    else:
        userprofile = Userprofile()
        userform = Userform()
    return render(request , 'signup.html' ,{'user_form':userform ,'profile_form':userprofile })


