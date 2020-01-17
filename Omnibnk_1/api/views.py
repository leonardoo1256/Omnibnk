from django.shortcuts import render
from api.models import Movie, User
from api.serializers import MovieSerializer, UserSerializer
from rest_framework import generics
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponseRedirect, Http404
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets


class Login(APIView):
    def post(self, request):
        data = request.data
        try:
            username = data['username']
            password = data['password']
            if len(User.objects.all().filter(username=username).filter(password= None).values()) > 0:
                return Response(data='yes', status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


class UserViewSets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MovieViewSets(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
#    def retrieve(self, request, *args, **kwargs):
 #       if len(request.data) > 0:


