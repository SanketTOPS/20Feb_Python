from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import *
from .serializer import *
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


@api_view(['GET'])
def getall(request):
    stdata=studinfo.objects.all()
    serial=studSerial(stdata,many=True)
    return Response(data=serial.data,status=status.HTTP_200_OK)


@api_view(['GET'])
def getstid(request,id):
    try:
        stid=studinfo.objects.get(id=id)
    except studinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serial=studSerial(stid)
    return Response(data=serial.data,status=status.HTTP_200_OK)