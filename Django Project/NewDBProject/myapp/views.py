from django.shortcuts import render,redirect
from .forms import *

# Create your views here.

def index(request):
    if request.method=='POST':
        stdata=studform(request.POST)
        if stdata.is_valid():
            stdata.save()
            print("Record inserted!")
        else:
            print(stdata.errors)
    return render(request,'index.html')

def showdata(request):
    stdata=studinfo.objects.all()
    return render(request,'showdata.html',{'stdata':stdata})

def updatedata(request,id):
    stid=studinfo.objects.get(id=id)
    if request.method=='POST':
        stdata=studform(request.POST,instance=stid)
        if stdata.is_valid():
            stdata.save()
            print("Record updated!")
            return redirect('showdata')
        else:
            print(stdata.errors)
    return render(request,'updatedata.html',{'stid':stid})

def deletedata(request,id):
    stid=studinfo.objects.get(id=id)
    studinfo.delete(stid)
    return redirect('showdata')
