from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class UserType(models.TextChoices):
        HUMAN = "human", "Human"
        AI = "ai", "AI"
        SERVICE = "service", "Service"

    user_type = models.CharField(max_length=16, choices=UserType.choices, default=UserType.HUMAN)
    job_title = models.CharField(max_length=160, blank=True)
    locale = models.CharField(max_length=8, default="en")
    theme = models.CharField(max_length=16, default="dark")
    mfa_enabled = models.BooleanField(default=False)
    mfa_secret = models.CharField(max_length=64, blank=True)
    disabled_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def is_human(self):
        return self.user_type == self.UserType.HUMAN
