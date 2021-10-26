from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
from . import validators
from django.utils.translation import gettext_lazy as _
from .constants import TYPE_GENDER, PRIORITY,STATUS, FEATURE, BUG, LABEL


class Notification(models.Model):
    message = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_date", ]

    def __str__(self):
        return ""


class User(AbstractUser):

    class Meta:
        ordering = ['id']

    phone_validator = validators.UnicodePhoneValidator

    avatar = CloudinaryField("avatar", null=True)
    gender = models.CharField(max_length=10, choices=TYPE_GENDER, default=0)
    email = models.EmailField(_('email address'), blank=True,unique=True)
    phone = models.CharField(max_length=10, null=True,unique=True,
        help_text=_('Enter a valid phone. This value may contain number, exactly 10 numbers'),
        validators=[phone_validator],
        error_messages={
            'unique': _("A user with that phone already exists."),
        })

    def __str__(self):
        return "username: {}".format(self.username)


class UserNotification(models.Model):

    user = models.ForeignKey(User, related_name='usenotifications',
        on_delete=models.PROTECT)
    notification = models.ForeignKey(Notification,
        related_name='usernotifications', on_delete=models.PROTECT)
    seen = models.BooleanField(default=False)
    sent_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Id: {}".format(self.pk)

    class Meta:
        ordering = ["-sent_date", "seen"]


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


class Epic(Base):
    leader = models.ForeignKey(User, related_name='epics_leading',
        on_delete=models.PROTECT)
    project = models.ForeignKey(User, related_name='epics',
        on_delete=models.PROTECT)


class UserEpic(models.Model):
    user = models.ForeignKey(User,related_name='userepics',
        on_delete=models.PROTECT)
    epic = models.ForeignKey(Epic, related_name='userepics',
        on_delete=models.PROTECT)
    joined_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return  "User: {},\nEpic: {}".format(self.user, self.epic.name)


class Task(Base):
    leader = models.ForeignKey(User, related_name='tasks_leading',
        on_delete=models.PROTECT)
    epic = models.ForeignKey(Epic, related_name='tasks', on_delete=models.PROTECT)
    priority = models.CharField(choices=PRIORITY, max_length=10, default=0)
    status = models.CharField(choices=STATUS,max_length=20, default=0)
    label = models.PositiveSmallIntegerField(choices=LABEL,default=FEATURE)


class UserTask(models.Model):
    user = models.ForeignKey(User, related_name='usertasks', on_delete=models.PROTECT)
    task = models.ForeignKey(Task, related_name='usertasks', on_delete=models.PROTECT)
    joined_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "User: {},\nTask: {}".format(self.user, self.task.name)

    class Meta:
        ordering = ["-task__created_date"]


class LauchTimeLine(models.Model):
    project = models.ForeignKey(Project, related_name='lauchtimelines',
        on_delete=models.CASCADE)
    time = models.DateTimeField()
    name = models.CharField(max_length=250)


    class Meta:
        ordering = ['-project__created_date']

    def __str__(self):
        return "Name: {},\n".format(self.name)


class Comment(models.Model):
    user = models.ForeignKey(User, related_name='comments', on_delete=models.PROTECT)
    task = models.ForeignKey(Task, related_name='comments', on_delete=models.PROTECT)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_date']
