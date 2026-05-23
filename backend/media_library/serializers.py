from rest_framework import serializers

from media_library.models import Attachment


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = "__all__"
        read_only_fields = ["uploaded_by", "created_at"]
