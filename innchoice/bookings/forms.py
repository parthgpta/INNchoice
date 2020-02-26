from django import forms
from .models import  timeslots


class edittime(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CaseForm, self).__init__(*args, **kwargs)
    class Meta:
        model = timeslots
        fields = ['starttime' , 'endtime']


class change(forms.Form):
    starttime = forms.IntegerField()
    endtime = forms.IntegerField()

    class Meta:
        fields = ( 'starttime' ,'endtime',)
