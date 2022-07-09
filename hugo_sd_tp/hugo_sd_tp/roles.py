from rest_framework import permissions, exceptions

READ_ONLY_METHODS = ['GET', 'HEAD', 'OPTIONS']


class Permissions(permissions.BasePermission):

    def has_permission(self, request, view):
        user = request.user
        if request.method in READ_ONLY_METHODS or user.is_staff and user.is_authenticated:
            return (user, None)
        else:
            raise exceptions.PermissionDenied()
