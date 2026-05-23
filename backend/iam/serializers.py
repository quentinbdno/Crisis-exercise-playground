from rest_framework import serializers

from iam.models import CrisisCell, Permission, Role


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = "__all__"


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"


class CrisisCellSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrisisCell
        fields = "__all__"
