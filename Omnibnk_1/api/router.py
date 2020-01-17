from rest_framework import routers
from api.views import UserViewSets, MovieViewSets

router = routers.DefaultRouter()
router.register('create/user', viewset=UserViewSets)
router.register('movie', viewset=MovieViewSets)

