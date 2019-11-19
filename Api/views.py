from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializers
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import viewsets
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


class UserView(APIView):

    def get(self, request):
        queryset = User.objects.all()
        serializer_class = UserSerializers(queryset,many=True)
        return Response(serializer_class.data)

    def post(self, request):
        data = request.data
        print(data)
        serializer = UserSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


















# def userview(request):
#
#     if request.method == 'GET':
#         users = User.objects.all()
#         user_class = UserSerializers(users, many=True,context={'request': request})
#         return JsonResponse(user_class.data, safe=False)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = UserSerializers(data=data)
#         if serializer.is_valid():
#             serialized = serializer.save()
#             return JsonResponse(serialized.data,status=201)
#         return JsonResponse(serializer.errors,status=400)

