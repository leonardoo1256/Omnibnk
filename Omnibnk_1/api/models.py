from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=100, unique= True, blank=False)
    genre = models.CharField(max_length=100, blank=False)
    director = models.CharField(max_length=100, blank=False)

    class Meta:
        ordering = ('id',)
        default_permissions = ('add','change','delete','view')

class TvShow(models.Model):
    name = models.CharField(max_length=100, unique= True, blank=False)
    genre = models.CharField(max_length=100, blank=False)
    director = models.CharField(max_length=100, blank=False)

    class Meta:
        ordering = ('id',)
        default_permissions = ('add','change','delete','view')

