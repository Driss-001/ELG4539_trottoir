from django.shortcuts import render
from rest_framework import viewsets
from .serializer import MyappSerializer,PiStateSerializer
from .models import Myapp,PiState

class MyappView(viewsets.ModelViewSet):
    
    serializer_class = MyappSerializer
    queryset = Myapp.objects.all()

class PiStateView(viewsets.ModelViewSet):

    serializer_class = PiStateSerializer
    queryset = PiState.objects.all()

# Create your views here.
