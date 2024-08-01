from django.shortcuts import render,redirect
from .forms import *


# Create your views here.

def index(request):
    if request.method=='POST':
        r=request.POST['role']
        u=request.POST['username']
        p=request.POST['password']

        user=users.objects.filter(role=r,username=u,password=p)
        if user:
            print("Login Successfull!")
            return redirect('home')
        else:
            print('Error!Login faild...')
    return render(request,'index.html')

def signup(request):
    if request.method=='POST':
        newuser=userForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            print("User created!")
            return redirect('/')
        else:
            print(newuser.errors)
    return render(request,'signup.html')

def home(request):
    return render(request,'home.html')