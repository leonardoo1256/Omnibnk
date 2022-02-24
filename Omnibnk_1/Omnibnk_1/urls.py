"""Omnibnk_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.conf.urls import url, include
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, logout_then_login, MovieViewSets

from api import views
from api.router import router

router = SimpleRouter()
router.register(r'moviees', MovieViewSets)

urlpatterns = [

    path('createuser', views.newuser),
    path('movies', views.movies),
    path('createmovie', views.createmovie),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('movie/<int:id>/delete/', views.delete, name="delete"),
    path('movie/<int:id>/update/', views.update, name="update"),
    path("accounts/login/", LoginView.as_view(), name="login"),
    path("logout/", logout_then_login, name='logout'),
    path('newuser', views.Newuser.as_view())

]
