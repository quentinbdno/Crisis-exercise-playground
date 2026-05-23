from rest_framework import viewsets

from media_library.models import Attachment
from media_library.serializers import AttachmentSerializer


class AttachmentViewSet(viewsets.ModelViewSet):
    queryset = Attachment.objects.select_related("uploaded_by", "scenario")
    serializer_class = AttachmentSerializer

    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user)
