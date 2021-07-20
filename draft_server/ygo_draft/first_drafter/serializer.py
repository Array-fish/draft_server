from rest_framework import serializers
from first_drafter.models import Room, Pack
from django.contrib.auth.models import User


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'players', 'current_player', 'player_num', 'pack_manager']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'rooms']


class PackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pack
        field = ['id', 'pack_manager', 'card']