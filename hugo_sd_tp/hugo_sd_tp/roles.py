from rest_framework import permissions, exceptions

READ_ONLY_METHODS = ['GET', 'HEAD', 'OPTIONS']


class Permissions(permissions.BasePermission):

    def has_permission(self, request, view):
        user = request.user
        if not user.is_authenticated:
            return exceptions.NotAuthenticated();

        if user.is_staff:
            return (user, None)

        if request.method in READ_ONLY_METHODS:
            return (user, None)
        else:
            raise exceptions.PermissionDenied()
