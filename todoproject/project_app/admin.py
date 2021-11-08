import sys
sys.path.append("..")

from django.contrib import admin
from django.contrib.auth.models import Permission

from user_app.models import User
from .models import Project


admin.site.register(User)
admin.site.register(Project)
admin.site.register(Permission)