from rest_framework import permissions
class IsOwnerPermission(permission.BasePermission):
    def has_permission(self, request, view):

        id request.user.is_authenticated:
        return True

    def has_object_permission(self, request, view, obj):
        if request.user,is_superuser:
            return True

        if request.method in permissions.SAFE_METHODs:
            return True

        if obj.owner == str(request.user):
            print('owner is same as requester...')
            return True

        return False
