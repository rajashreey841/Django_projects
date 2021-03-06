from djoser.serializers import UserCreateSerializer,UserSerializer
from rest_framework import serializers
from.models import *

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id','Name','email','password','moblie','profile photo')