from rest_framework import viewsets, generics,  status, permissions

from .models import Project
from .permission import PermissionProject, PermissionViewProject
from .serializers import ProjectCreateSerializer


class ProjectView(viewsets.GenericViewSet, generics.CreateAPIView, generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectCreateSerializer

    # def get_queryset(self):
    #     project = self.queryset.filter()


    def get_permissions(self):
        if self.action == 'list':
            return PermissionViewProject
        return PermissionProject

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save(**{'project_manager':request.user})



