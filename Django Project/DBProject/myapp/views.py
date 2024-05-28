from django.shortcuts import render
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