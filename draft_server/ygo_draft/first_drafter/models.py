from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    current_player = models.IntegerField(default=0)
    player_cnt = models.IntegerField(default=0)
    player_num = models.IntegerField(default=2)


class PackManager(models.Model):
    room = models.ForeignKey(Room, related_name="pack_manager", on_delete=models.CASCADE)
    current_pack_cnt = models.IntegerField(default=0)


class Pack(models.Model):
    pack_manager = models.ForeignKey(PackManager, related_name="pack", on_delete=models.CASCADE)


class Card(models.Model):
    card_id = models.IntegerField()
    pack = models.ForeignKey(Pack, related_name="card", on_delete=models.CASCADE)


class UserRoomRelation(models.Model):
    user = models.OneToOneField(User, related_name="room_relation")
    room = models.ForeignKey(Room, related_name="user_relation", on_delete=models.CASCADE)
    player_idx = models.IntegerField(null=False, default=0)
