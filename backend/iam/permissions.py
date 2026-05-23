from rest_framework.permissions import BasePermission


class HasPlatformPermission(BasePermission):
    required_permission = ""

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        if request.user.is_superuser:
            return True
        required = getattr(view, "required_permission", self.required_permission)
        if not required:
            return True
        assignments = request.user.role_assignments.select_related("role").prefetch_related("role__permissions")
        return any(permission.key == required for assignment in assignments for permission in assignment.role.permissions.all())
