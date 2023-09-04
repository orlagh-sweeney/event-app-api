from rest_framework import permissions


class IsAuthenticatedOrIsOwner(permissions.BasePermission):
    """
    Users must be logged in to view the object
    Only the object owner can edit the object
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated
        return obj.owner == request.user


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Any site user can view the object
    Only the object owner can edit the object
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user

