from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Profile, Post
from .serializers import ProfileSerializer, PostsSerializer
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django.contrib.auth.models import User
import json

# @csrf_exempt
def profile_list(request):
    if request.method == "GET":
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = ProfileSerializer(data=data)
        # Profile.last_request = datetime.now()

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def user_profile(request, pk):
    try:
        profile = Profile.objects.get(id=pk)

    except Profile.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = ProfileSerializer(profile)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = ProfileSerializer(profile, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        profile.delete()
        return HttpResponse(status=204)


@csrf_exempt
def posts_list(request):
    if request.method == "GET":
        profiles = Post.objects.all()
        serializer = PostsSerializer(profiles, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = PostsSerializer(data=data)
        # Profile.last_request = datetime.now()

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)
