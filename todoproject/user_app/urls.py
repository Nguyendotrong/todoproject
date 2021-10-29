from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register('users',views.UserViewSet)

urlpatterns = [

    # path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('', include(router.urls)),


]