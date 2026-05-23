from django.contrib import admin

from audit.models import AuditLog


@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ("created_at", "action", "actor", "resource_type", "resource_id")
    list_filter = ("action", "resource_type")
    search_fields = ("action", "resource_id", "correlation_id")
