from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from .models import *
from .serializers import DepartmentSerializer, ResourceSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class DepartmentView(ModelViewSet):
    queryset=Department.objects.all()
    serializer_class = DepartmentSerializer     #during communication between frontend and backend json is used

class ResourceView(GenericAPIView):
    queryset=Resource.objects.all()
    serializer_class=ResourceSerializer

    def get(self,request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset,many=True) # when (many=True) it converts every single object from queryset into json
        return Response(serializer.data) #returns the converted json data
    
    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Data Created')
        else:
            return Response(serializer.errors)
        
class ResourceDetailView(GenericAPIView):
    queryset = Resource.objects.all()
    serializer_class=ResourceSerializer

    def get(self,request,pk):
        try:
            queryset = Resource.objects.get(id=pk)
        except:
            return Response('Data not found!',status=status.HTTP_404_NOT_FOUND)
        serializer=self.serializer_class(queryset)
        return Response(serializer.data)

    def put(self,request,pk):
        serializer = self.serializer_class(data=request.data)
        try:
            queryset = Resource.objects.get(id=pk)
        except:
            return Response('Data not found!',status=status.HTTP_404_NOT_FOUND)
        serializer=self.serializer_class(queryset,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Data updated')
        else:
            return Response(serializer.errors)
        
    def delete(self,request,pk):
        try:
            queryset = Resource.objects.get(id=pk)
        except:
            return Response('Data not found!',status=status.HTTP_404_NOT_FOUND)
        queryset.delete()
        return Response('Data deleted!')
