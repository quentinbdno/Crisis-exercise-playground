from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from iam.models import CrisisCell, Permission, Role
from iam.serializers import CrisisCellSerializer, PermissionSerializer, RoleSerializer


class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [IsAdminUser]


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.prefetch_related("permissions", "inherits")
    serializer_class = RoleSerializer
    permission_classes = [IsAdminUser]


class CrisisCellViewSet(viewsets.ModelViewSet):
    queryset = CrisisCell.objects.prefetch_related("members", "roles")
    serializer_class = CrisisCellSerializer
    permission_classes = [IsAdminUser]
