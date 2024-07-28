from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsOwnerOrReadOnly(BasePermission):
    """
    Доступ для создателя или безопасные методы.
    """
    def has_permission(self, request, view):
        return (request.method in SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return (request.method in SAFE_METHODS
                or (request.user == obj.user
                    or request.user.is_moderator
                    or request.user.is_admin
                    or request.user.is_superuser
                    )
                )
