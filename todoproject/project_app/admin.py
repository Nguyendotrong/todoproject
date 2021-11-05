from django.contrib import admin
from django.contrib.auth.models import Permission

# Register your models here.
from .models import Project

admin.site.register(Project)
admin.site.register(Permission)