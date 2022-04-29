from .models import Profile, FollowUnfollow
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class FollowUnfollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = FollowUnfollow
        fields = '__all__'


class FollowUnfollowSerializerSorted(serializers.ModelSerializer):
    class Meta:
        model = FollowUnfollow
        fields = ("user_id", "profile")
