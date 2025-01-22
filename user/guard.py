from rest_framework.permissions import BasePermission

class IsPrincipalOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow only the principal to perform write operations
        return request.method in ('GET', 'HEAD', 'OPTIONS') or obj.principal.id == request.user.id
