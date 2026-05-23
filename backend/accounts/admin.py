from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import User


@admin.register(User)
class CrisisUserAdmin(UserAdmin):
    list_display = ("email", "username", "user_type", "mfa_enabled", "is_active", "is_staff")
    list_filter = ("user_type", "mfa_enabled", "is_active", "is_staff")
    fieldsets = UserAdmin.fieldsets + (("Crisis platform", {"fields": ("user_type", "job_title", "locale", "theme", "mfa_enabled", "mfa_secret", "disabled_at")}),)
