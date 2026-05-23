from django.db import models


class Stimulus(models.Model):
    class StimulusType(models.TextChoices):
        CHAT_MESSAGE = "chat_message", "Chat message"
        EMAIL = "email", "Email"
        FAKE_TWEET = "fake_tweet", "Fake tweet"
        FAKE_NEWS = "fake_news", "Fake news"
        VOICE_CALL = "voice_call", "Voice call"
        SYSTEM_NOTIFICATION = "system_notification", "System notification"
        VIDEO = "video", "Video"
        ATTACHMENT = "attachment", "Attachment"

    class DeliveryChannel(models.TextChoices):
        PUBLIC_CHANNEL = "public_channel", "Public channel"
        PRIVATE_CHANNEL = "private_channel", "Private channel"
        DIRECT_MESSAGE = "direct_message", "Direct message"
        EMAIL = "email", "Email"
        SYSTEM = "system", "System"

    scenario = models.ForeignKey("scenarios.Scenario", on_delete=models.CASCADE, related_name="stimuli")
    planned_time_seconds = models.PositiveIntegerField(default=0)
    sender_label = models.CharField(max_length=160)
    recipient_label = models.CharField(max_length=240, blank=True)
    stimulus_type = models.CharField(max_length=32, choices=StimulusType.choices)
    delivery_channel = models.CharField(max_length=32, choices=DeliveryChannel.choices)
    subject = models.CharField(max_length=240, blank=True)
    body = models.TextField(blank=True)
    payload = models.JSONField(default=dict, blank=True)
    attachments = models.ManyToManyField("media_library.Attachment", blank=True, related_name="stimuli")
    ai_agent = models.ForeignKey("ai_agents.AIAgent", null=True, blank=True, on_delete=models.SET_NULL, related_name="stimuli")
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["planned_time_seconds", "order"]
