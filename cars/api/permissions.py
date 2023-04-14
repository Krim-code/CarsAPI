from rest_framework import permissions


class PostGetForAllOthersForUserOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'POST', 'OPTIONS']:
            return True
        return obj.author_email == request.user.email or \
            bool(request.user and request.user.is_staff)
