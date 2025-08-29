from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission: Only the creator of the object can edit or delete it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed for any request (safe methods)
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the creator of the recipe
        return obj.created_by == request.user
