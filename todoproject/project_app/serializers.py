from rest_framework.fields import ImageField
from rest_framework.serializers import ModelSerializer

from .models import Project


class ProjectCreateSerializer(ModelSerializer):

    class Meta:
        model = Project
    image = ImageField(required=True, error_messages={'required': 'Lỗi upload avatar'})
    exclude = ['project_manager',]
