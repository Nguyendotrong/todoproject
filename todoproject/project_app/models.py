import sys
sys.path.append("..")

from django.db import models
from cloudinary.models import CloudinaryField

from user_app.models import User


class Base(models.Model):

    name = models.CharField(max_length=250, )
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    completed_date = models.DateTimeField()
    is_active  = models.BooleanField()

    class Meta:
        abstract = True
        ordering = ['-created_date', ]

    def __str__(self):
        return "Name: {},\nDescription: {}".format(self.name,self.description)


class Project(Base):
    image = CloudinaryField('image', null=True)
    project_manager = models.ForeignKey(User,
        related_name='propjects_manager', on_delete=models.PROTECT)



class UserProject(models.Model):
    user = models.ForeignKey(User,
        related_name='UserProjects', on_delete=models.PROTECT)
    project = models.ForeignKey(Project,
        related_name='UserProjects', on_delete=models.PROTECT)
    joined_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return  "User: {},\nProject: {}".format(self.user, self.project.name)
