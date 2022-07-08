from rest_framework import permissions, exceptions


class RolesPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        user = request.user
        if user.is_staff and user.is_authenticated:
            return (user, None)
        else:
            data = {
                'code': 403,
                'data': 'Não autorizado.'
            }
            raise exceptions.APIException(data)
