from django.urls import path, re_path, include
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register('users',views.UserViewSet)

urlpatterns = [

    path('', include(router.urls)),

]
