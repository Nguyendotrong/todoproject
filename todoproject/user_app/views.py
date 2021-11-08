from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, generics,status, permissions
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import User
from .serializers import UserCreateSerializer, UserSerializer


class UserViewSet(viewsets.GenericViewSet, generics.CreateAPIView, generics.ListAPIView):

    queryset = User.objects.filter(is_active=True)
    parser_classes = [MultiPartParser, ]


    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny(),]
        return [IsAuthenticated(),]

    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        return UserSerializer

    # def list(self, request, *args, **kwargs):
    #     pass

    @swagger_auto_schema(
        operation_description=' get profile of current user',
        responses={
            status.HTTP_200_OK: UserSerializer()
        }
    )
    @action(methods=['get'], detail=False, url_path='current-user')
    def current_user(self, request):
        return Response(self.get_serializer(request.user).data)


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



