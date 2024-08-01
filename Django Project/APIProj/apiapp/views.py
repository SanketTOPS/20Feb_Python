from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *
import requests

# Create your views here.

def index(request):
    #stdata=studinfo.objects.all()
    url="http://127.0.0.1:8000/getall/"
    req=requests.get(url)
    data=req.json()
    return render(request,'index.html',{'data':data})


@api_view(['GET'])
def getall(request):
    stdata=studinfo.objects.all()
    serial=studSerial(stdata,many=True)
    return Response(data=serial.data,status=status.HTTP_200_OK)


@api_view(['GET'])
def getid(request,id):
    try:
        stid=studinfo.objects.get(id=id)
    except studinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serial=studSerial(stid)
    return Response(data=serial.data,status=status.HTTP_200_OK)


@api_view(['GET','DELETE'])
def deleteid(request,id):
    try:
        stid=studinfo.objects.get(id=id)
    except studinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serial=studSerial(stid)
        return Response(data=serial.data,status=status.HTTP_200_OK)
    if request.method=='DELETE':
        studinfo.delete(stid)
        return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['POST'])
def savedata(request):
    if request.method=='POST':
        serial=studSerial(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT'])
def updatedata(request,id):
    try:
        stid=studinfo.objects.get(id=id)
    except studinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serial=studSerial(stid)
        return Response(data=serial.data,status=status.HTTP_200_OK)
    if request.method=='PUT':
        serial=studSerial(data=request.data,instance=stid)
        if serial.is_valid():
            serial.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    
