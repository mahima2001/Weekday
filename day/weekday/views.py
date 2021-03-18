from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
from django.shortcuts import render
import datetime

# Create your views here.
class NewTaskForm(forms.Form):
     day = forms.IntegerField(label="Enter Date",max_value=31,min_value=1)
     month = forms.ChoiceField(choices=[(1,'JAN'),(2,'FEB'),(3,'MAR'),(4,'APR'),(5,'MAY'),(6,'JUN'),(7,'JUL'),(8,'AUG'),(9,'SEP'),(10,'OCT'),(11,'NOV'),(12,'DEC')])
     year = forms.IntegerField(label="Enter Year")
def fun(date,month,year):
    d1={0:0,1:5,2:3,3:1}
    d2={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    d3={0:'SUNDAY',1:'MONDAY',2:'TUESDAY',3:'WEDNESDAY',4:'THURSDAY',5:'FRIDAY',6:'SATURDAY'}
    l=year//100
    t=d1[l%4] 
    p=(year%100)-1
    h=(p+(p//4))%7
    print(h,p,t)
    f=date
    for j in range(1,month):
        f+=d2[j]
    return(d3[f%7+h+t])
def index(request):
    if request.method =="POST":
        form=NewTaskForm(request.POST)
        if form.is_valid():
            date=form.cleaned_data['day']
            month=int(form.cleaned_data['month'])
            year=form.cleaned_data['year']
        print(type(month),month)
        s=fun(date,month,year)
        return render(request,'weekday/index.html',{
        'form':form,
        'wkdy':s
        })
        form=NewTaskForm()
    now=datetime.datetime.today()
    form=NewTaskForm()
    form.fields['day'].initial = now.date
    return render(request,'weekday/index.html',{
        'form':form,
        
        })
     