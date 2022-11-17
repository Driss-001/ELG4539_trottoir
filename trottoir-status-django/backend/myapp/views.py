from django.shortcuts import render
from rest_framework import viewsets
from .serializer import MyappSerializer
from .models import Myapp

class MyappView(viewsets.ModelViewSet):
    
    serializer_class = MyappSerializer
    queryset = Myapp.objects.all()

# Create your views here.
