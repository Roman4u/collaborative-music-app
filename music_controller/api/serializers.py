# this file will take our db model, all of the python related code, and
# translate this room into a JSON response
# for example, it will take all of the keys and values, 
# turn them into strings and place them within an object literal

from dataclasses import fields
from rest_framework import serializers
from .models import Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'code', 'host', 'guest_can_pause', 'vote_to_skip', 'created_at')