from django.contrib import admin

from iam.models import CrisisCell, Permission, Role, UserRoleAssignment

admin.site.register(Permission)
admin.site.register(Role)
admin.site.register(CrisisCell)
admin.site.register(UserRoleAssignment)
