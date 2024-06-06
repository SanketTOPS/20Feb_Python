from django.shortcuts import render
from .forms import *

# Create your views here.
def index(request):
    return render(request,'index.html')

def error(request):
    return render(request,'404.html')

def blog(request):
    return render(request,'blog.html')

def contact(request):
    if request.method=='POST':
        newreq=contactform(request.POST)
        if newreq.is_valid():
            newreq.save()
            print("Your request has been submitted!")
        else:
            print(newreq.errors)
    return render(request,'contact.html')

def portfolio(request):
    return render(request,'portfolio.html')