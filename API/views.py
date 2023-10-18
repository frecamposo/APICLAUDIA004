from django.shortcuts import render
from .models import Receta,Repartidor
from .serializers import RecetaSerializers,RepartidorSerializers
from rest_framework import generics

# Create your views here.

class RecetaViewSet(generics.ListCreateAPIView  ):
    queryset = Receta.objects.all()
    serializer_class = RecetaSerializers


 
