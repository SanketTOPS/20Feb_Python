from django.shortcuts import render
import random

# Create your views here.
def index(request):
    name="Nirav"
    num=random.randint(1111,9999)
    return render(request,'index.html',{'nm':name,'num':num})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')