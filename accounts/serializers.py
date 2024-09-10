from .models import User, Follow
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'nickname', 'birth', 'introduction')

class FollowListSerializer(serializers.ModelSerializer):
    follower = UserSerializer()
    followed = UserSerializer()

    class Meta:
        model = Follow
        fields = ['follower', 'followed']