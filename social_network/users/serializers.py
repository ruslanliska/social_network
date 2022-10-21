from rest_framework import serializers
from .models import Profile, Post


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

