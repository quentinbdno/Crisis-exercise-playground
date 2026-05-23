from django.conf import settings
from django.db import models


class Permission(models.Model):
    key = models.CharField(max_length=120, unique=True)
    name = models.CharField(max_length=160)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.key


class Role(models.Model):
    name = models.CharField(max_length=120, unique=True)
    description = models.TextField(blank=True)
    permissions = models.ManyToManyField(Permission, blank=True, related_name="roles")
    inherits = models.ManyToManyField("self", blank=True, symmetrical=False, related_name="children")

    def __str__(self):
        return self.name


class CrisisCell(models.Model):
    name = models.CharField(max_length=160)
    description = models.TextField(blank=True)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="crisis_cells")
    roles = models.ManyToManyField(Role, blank=True, related_name="crisis_cells")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class UserRoleAssignment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="role_assignments")
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    crisis_cell = models.ForeignKey(CrisisCell, null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "role", "crisis_cell")
