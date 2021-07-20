from first_drafter.models import Room, PackManager, Pack, Card
from first_drafter.serializers import RoomSerializer, UserSerializer
from rest_framework import generics, permissions
from first_drafter.permissons import IsJoinOrReadOnly
from django.contrib.auth.models import User


# Create your views here.
class RoomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permissions = [permissions.IsAuthenticatedOrReadOnly, IsJoinOrReadOnly]


class UserDetail(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

