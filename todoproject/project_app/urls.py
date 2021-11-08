from django.urls import path, re_path, include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register('',views.ProjectView)

urlpatterns = [

    # path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('', include(router.urls)),


]
