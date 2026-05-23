from django.conf import settings
from django.db import models


class Attachment(models.Model):
    class MediaType(models.TextChoices):
        IMAGE = "image", "Image"
        PDF = "pdf", "PDF"
        VIDEO = "video", "Video"
        DOCUMENT = "document", "Document"
        AUDIO = "audio", "Audio"
        OTHER = "other", "Other"

    name = models.CharField(max_length=240)
    file = models.FileField(upload_to="attachments/")
    media_type = models.CharField(max_length=24, choices=MediaType.choices, default=MediaType.OTHER)
    mime_type = models.CharField(max_length=120, blank=True)
    size_bytes = models.PositiveBigIntegerField(default=0)
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    scenario = models.ForeignKey("scenarios.Scenario", null=True, blank=True, on_delete=models.CASCADE, related_name="attachments")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
