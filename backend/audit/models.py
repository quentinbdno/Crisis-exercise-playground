from django.conf import settings
from django.db import models


class AuditLog(models.Model):
    actor = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    action = models.CharField(max_length=160)
    resource_type = models.CharField(max_length=120, blank=True)
    resource_id = models.CharField(max_length=80, blank=True)
    exercise = models.ForeignKey("exercises.Exercise", null=True, blank=True, on_delete=models.SET_NULL)
    scenario = models.ForeignKey("scenarios.Scenario", null=True, blank=True, on_delete=models.SET_NULL)
    correlation_id = models.CharField(max_length=120, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    metadata = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
