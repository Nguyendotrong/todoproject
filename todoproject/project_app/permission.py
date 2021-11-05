from rest_framework.permissions import IsAuthenticated

class PermissionProject(IsAuthenticated):
    def has_permission(self, request, view):
        return super().has_permission(request,view)\
            and request.user.has_perms(['project_app.add_project',
                                        'project_app.change_project',
                                        'project_app.delete_project'])

class PermissionViewProject(IsAuthenticated):

    def has_permission(self, request, view):
        return super().has_permission(request,view)\
            and request.user.has_perm('project_app.view_project')