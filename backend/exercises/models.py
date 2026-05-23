from django.conf import settings
from django.db import models


class Exercise(models.Model):
    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        SCHEDULED = "scheduled", "Scheduled"
        RUNNING = "running", "Running"
        PAUSED = "paused", "Paused"
        COMPLETED = "completed", "Completed"
        CANCELLED = "cancelled", "Cancelled"

    name = models.CharField(max_length=200)
    scenario = models.ForeignKey("scenarios.Scenario", on_delete=models.PROTECT, related_name="exercises")
    status = models.CharField(max_length=24, choices=Status.choices, default=Status.DRAFT)
    starts_at = models.DateTimeField(null=True, blank=True)
    ended_at = models.DateTimeField(null=True, blank=True)
    timeline_speed = models.DecimalField(max_digits=5, decimal_places=2, default=1)
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="exercises")
    crisis_cells = models.ManyToManyField("iam.CrisisCell", blank=True, related_name="exercises")
    metadata = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ExerciseRoom(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name="rooms")
    name = models.CharField(max_length=160)
    crisis_cell = models.ForeignKey("iam.CrisisCell", null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)


class StimulusDelivery(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        SCHEDULED = "scheduled", "Scheduled"
        DELIVERED = "delivered", "Delivered"
        FAILED = "failed", "Failed"
        RESENT = "resent", "Resent"

    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name="stimulus_deliveries")
    stimulus = models.ForeignKey("stimuli.Stimulus", on_delete=models.CASCADE, related_name="deliveries")
    status = models.CharField(max_length=24, choices=Status.choices, default=Status.PENDING)
    scheduled_for = models.DateTimeField(null=True, blank=True)
    delivered_at = models.DateTimeField(null=True, blank=True)
    error = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
