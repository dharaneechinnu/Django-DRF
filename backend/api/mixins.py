from .permissions import IsStaffEditorPermission

from rest_framework import permissions

class IsStaffEditorPermissionMixins():
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]


class UserQuerySetMixins():
    user_field = 'user'
    allow_staff_view = False
    def get_queryset(self):
        qs = super().get_queryset()   # get base queryset
        lookup = {self.user_field: self.request.user}
        return qs.filter(**lookup)
