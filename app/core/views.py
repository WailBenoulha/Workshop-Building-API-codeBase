from django.shortcuts import render

from rest_framework.views import APIView
from .models import Task
from .serializers import Taskserializer
from rest_framework.response import Response
from rest_framework import status

class taskview(APIView):
    def get(self,request):
        model = Task.objects.all()
        serializer = Taskserializer(model,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request):
        serializer = Taskserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
