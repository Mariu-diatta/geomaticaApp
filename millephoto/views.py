from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from .models import Users,Album,Photo
from .serializers import UsersSerializer,AlbumSerializer,PhotoSerializer
from rest_framework.decorators import api_view
from rest_framework import status


#Liste d'utilisateur
@api_view(['GET','POST','DELETE'])
def UsersList(request):

    if request.method=='GET':
        users=Users.objects.all()
        user_serial=UsersSerializer(users,many=True)
        return  Response(user_serial.data)

    elif request.method=='POST':
        data_serial=UsersSerializer(data=request.data)
        if data_serial.is_valid():
            data_serial.save()
            return  Response(data_serial.data,status=status.HTTP_201_CREATED)
        return Response(data_serial.errors,status=status.HTTP_400_BAD_REQUEST)

#liste des album
@api_view(['GET','POST','DELETE'])
def AlbumList(request):

    if request.method=='GET':
        albums=Album.objects.all()
        albums_serial=AlbumSerializer(Album,many=True)
        return JsonResponse(albums_serial.data, safe=False)

    elif request.method=='POST':
        data1_serial=AlbumSerializer(data=request.data1)
        if data1_serial.is_valid():
            data1_serial.save()
            return  Response(data1_serial.data,status=status.HTTP_201_CREATED)
        return Response(data1_serial.errors,status=status.HTTP_400_BAD_REQUEST)

#les photos
@api_view(['GET','POST','DELETE'])
def PhotoList(request):

    if request.method=='GET':
        photos=Photo.objects.all()
        photos_serial=AlbumSerializer(Photo,many=True)
        return  JsonResponse(photos_serial.data,safe=False)

    elif request.method=='POST':
        data2_serial=AlbumSerializer(data=request.data2)
        if data2_serial.is_valid():
            data2_serial.save()
            return  Response(data2_serial.data,status=status.HTTP_201_CREATED)
        return Response(data2_serial.errors,status=status.HTTP_400_BAD_REQUEST)