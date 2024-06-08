from django.shortcuts import render,redirect
from .forms import *

# Create your views here.

def index(request):
    return render(request,'index.html')

def regi(request):
    if request.method=='POST':
        newreq=signupForm(request.POST)
        if newreq.is_valid():
            newreq.save()
            print("Signup successfully!")
            return redirect('/')
        else:
            print(newreq.errors)
    return render(request,'regi.html')

def home(request):
    return render(request,'home.html')