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
from django.contrib import admin
from django.urls import path
from api.api import UserApi
from api import views
from django.conf.urls import url, include
from api.router import router
from django.contrib.auth.views import LoginView
#from rest_framework.authtoken import views


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('login/', LoginView.as_view(template_name='registration/login.html'), name="login"),
    path('api/authenticate', views.Login.as_view(), name="auth"),
    path('api/', include(router.urls)),
    #re_path(r'^api/movie/$',views.MovieList.as_view(), name = 'movie'),
    #re_path(r'^api/movie/(?P<pk>[0-9]+)/$', views.MovieDetail.as_view(), name = 'movies')

]
