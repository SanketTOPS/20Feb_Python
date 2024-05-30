from django.shortcuts import render,HttpResponse,redirect
from .forms import *

# Create your views here.
def index(request):
    if request.method=='POST':
        req=studform(request.POST)
        if req.is_valid():
            req.save()
            print("Record inserted!")
        else:
            print(req.errors)
    return render(request,'index.html')

def showdata(request):
    stdata=studinfo.objects.all()
    return render(request,'showdata.html',{'stdata':stdata})

def updatedata(request):
    return render(request,'updatedata.html')

def deletedata(request,id):
    stid=studinfo.objects.get(id=id)
    studinfo.delete(stid)
    return redirect('showdata')

    