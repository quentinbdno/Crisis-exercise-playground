from django.conf import settings
from django.db import models


class Channel(models.Model):
    class ChannelType(models.TextChoices):
        PUBLIC = "public", "Public"
        PRIVATE = "private", "Private"
        DIRECT = "direct", "Direct"

    exercise = models.ForeignKey("exercises.Exercise", on_delete=models.CASCADE, related_name="channels")
    name = models.CharField(max_length=160)
    channel_type = models.CharField(max_length=24, choices=ChannelType.choices, default=ChannelType.PUBLIC)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="channels")
    crisis_cells = models.ManyToManyField("iam.CrisisCell", blank=True, related_name="channels")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.exercise_id}:{self.name}"


class Message(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name="messages")
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    sender_label = models.CharField(max_length=160, blank=True)
    body = models.TextField()
    is_ai_generated = models.BooleanField(default=False)
    stimulus = models.ForeignKey("stimuli.Stimulus", null=True, blank=True, on_delete=models.SET_NULL)
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE, related_name="thread_replies")
    pinned = models.BooleanField(default=False)
    reactions = models.JSONField(default=dict, blank=True)
    attachments = models.ManyToManyField("media_library.Attachment", blank=True, related_name="messages")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]


class DirectMessage(models.Model):
    exercise = models.ForeignKey("exercises.Exercise", on_delete=models.CASCADE, related_name="direct_messages")
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="direct_threads")
    created_at = models.DateTimeField(auto_now_add=True)
