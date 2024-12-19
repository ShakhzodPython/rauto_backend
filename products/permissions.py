from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Пользователь является автором поста или только для чтения.
    """

    def has_object_permission(self, request, view, obj):
        # Разрешить GET, HEAD или OPTIONS запросы всем.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Разрешить изменение или удаление только автору поста.
        return obj.author == request.user

