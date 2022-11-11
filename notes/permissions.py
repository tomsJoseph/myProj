from rest_framework import permissions

class AdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
             return request.user.is_superuser


# following is a class for explaining the concept, please don't use it.
class OwnerOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
         return obj.creator == request.user

