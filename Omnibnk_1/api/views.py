from django.contrib.auth.models import User
from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from rest_framework import status, viewsets
from rest_framework.views import APIView
from api.models import Movie
from api.serializers import MovieSerializer


def newuser(request):
    return render(request, 'create_user.html')


def movies(request):
    if request.user.is_authenticated:
        return render(request, 'movies.html')
    else:
        return HttpResponseNotFound(status=status.HTTP_401_UNAUTHORIZED)


def createmovie(request):
    if request.user.is_authenticated:
        return render(request, 'create_movie.html')
    else:
        return HttpResponseNotFound(status=status.HTTP_401_UNAUTHORIZED)


def delete(request, id):
    item = get_object_or_404(Movie, id=id)
    if request.method == "POST":
        item.delete()
    context = {
        "object": item
    }
    return render(request, "delete_movie.html", context)


def update(request, id):
    item = get_object_or_404(Movie, id=id)
    if request.method == "PATCH":
        item.save()
    context = {
        "object": item
    }
    return render(request, "update_movie.html", context)


class MovieViewSets(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class Newuser(APIView):
    def post(self, request):
        data = request.data
        username = data['username']
        password = data['password']
        try:
            user = User.objects.create_user(username, username + "@gmail.com", password)
            user.save()
            return render(request, 'registration/login.html')
        except:
            return render(request, 'create_user.html')
