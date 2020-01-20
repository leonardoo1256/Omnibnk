from rest_framework import routers
from api.views import MovieViewSets

router = routers.DefaultRouter()
router.register('movie', viewset=MovieViewSets, basename='movies')
router.register('create/movie', viewset=MovieViewSets, basename='createmovie')
