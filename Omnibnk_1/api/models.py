from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=100, blank=False)
    genre = models.CharField(max_length=100, blank=False)
    director = models.CharField(max_length=100, blank=False)

    class Meta:
        ordering = ('name',)

class User(models.Model):
    username = models.CharField(max_length=100, blank=False)
    password = models.CharField(max_length=100, blank=False)

    class Meta:
        ordering = ('username',)
