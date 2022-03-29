from django.shortcuts import render
from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room

# Create your views here.
# 


class RoomView(generics.ListAPIView):
    # will return all of the Room objects
    queryset = Room.objects.all()
    # RoomSerializer converts the db into a JSON object from .models file
    serializer_class = RoomSerializer