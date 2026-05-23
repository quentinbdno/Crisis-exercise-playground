from django.contrib.auth import authenticate
from rest_framework import serializers

from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    roles = serializers.SerializerMethodField()
    crisis_cells = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "username",
            "user_type",
            "job_title",
            "locale",
            "theme",
            "mfa_enabled",
            "is_active",
            "roles",
            "crisis_cells",
            "created_at",
        ]
        read_only_fields = ["created_at"]

    def get_roles(self, obj):
        return [assignment.role.name for assignment in obj.role_assignments.select_related("role")]


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        try:
            username = User.objects.get(email=attrs["email"]).username
        except User.DoesNotExist:
            username = attrs["email"]
        user = authenticate(username=username, password=attrs["password"])
        if not user:
            raise serializers.ValidationError("Invalid credentials")
        attrs["user"] = user
        return attrs
