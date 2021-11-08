from rest_framework.fields import ImageField
from rest_framework.serializers import ModelSerializer

from .models import Project


class ProjectCreateSerializer(ModelSerializer):
    image = ImageField(required=True, error_messages={'required': 'Lỗi upload avatar'})

    class Meta:
        model = Project
        exclude = ['project_manager',]

class ProjectSerializer(ProjectCreateSerializer):
    image = ImageField(required=True, error_messages={'required': 'Lỗi upload avatar'})
    class Meta:
        model = ProjectCreateSerializer.Meta.model

        exclude = ['id']
