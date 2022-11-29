from rest_framework import serializers
from .models import Myapp,PiState

#Data framework => help the frontend to work with the received data

class MyappSerializer(serializers.ModelSerializer):
        class Meta:
            model = Myapp
            fields = [
            'id', 
            'title',
            'description',
            'completed',
            ]


class PiStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PiState
        fields =[
            'RoadState',
            'LampState',

        ]

