from django.shortcuts import render,redirect
from .forms import *
from django.core.mail import send_mail
import random
from FinalProject import settings

# Create your views here.

def index(request):
    user=request.session.get('user')
    return render(request,'index.html',{'user':user})

def login(request):
    if request.method=='POST':
        unm=request.POST['username']
        pas=request.POST['password']

        user=usersignup.objects.filter(username=unm,password=pas)
        if user:
            print("Login Successfully!")
            request.session['user']=unm
            return redirect('/')
        else:
            print("Error!Login faild....")
    return render(request,'login.html')

def signup(request):
    if request.method=='POST':
        newuser=signupForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            print("Signup Successfully!")

            #Email Sending Code
            global otp
            otp=random.randint(11111,99999)
            sub="Your One Time Password"
            msg=f"Dear User\n\nThanks for registration with us!\n\nFor account verification, your one time password is below.\n\nYour One time password:{otp}\n\nThanks & Regards!\n+91 9724799469 | www.tops-int.com"
            from_email=settings.EMAIL_HOST_USER
            #to_email=["patelbhumi2504@gmail.com","ayushpatel5440@gmail.com","heetgokani8@gmail.com","vinaychhatraliya19@gmail.com"]
            to_email=[request.POST['username']]
            send_mail(subject=sub,message=msg,from_email=from_email,recipient_list=to_email)
            return redirect('otpverify')
        else:
            print(newuser.errors)
    return render(request,'signup.html')

def notes(request):
    return render(request,'notes.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def otpverify(request):
    global otp
    msg=""
    print("OTP:",otp)
    if request.method=='POST':
        if request.POST['otp']==str(otp):
            return redirect("login")
        else:
            print("Invalid OTP...Please try again!")
            msg="Invalid OTP...Please try again!"
    return render(request,'otpverify.html',{'msg':msg})