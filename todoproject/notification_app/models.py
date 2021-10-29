import sys
sys.path.append("..")
from django.db import models
from user_app.models import User



class Notification(models.Model):
    message = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_date", ]

    def __str__(self):
        return ""




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
