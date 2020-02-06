from django import forms
from django.contrib.auth.models import User
from . models import person


class Userprofile(forms.ModelForm):

    class Meta:
        model = person
        fields = ('name','gender' , 'dob','phone','user_type')

class Userform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    username = forms.CharField()
    class Meta():
        model = User
        fields = ('username','email','password',)