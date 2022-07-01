from rest_framework.permissions import BasePermission

class IsProjectOwnerOrReadOnly(BasePermission):
    """
    Permission to check if the user is a project owner
    """
    def has_permission(self, request, view):
        return request.user.is_admin

    # def has_object_permission(self, request, view, obj):
    #     return super().has_object_permission(request, view, obj)