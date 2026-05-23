from rest_framework import viewsets

from audit.services import audit
from messaging.models import Channel, Message
from messaging.serializers import ChannelSerializer, MessageSerializer


class ChannelViewSet(viewsets.ModelViewSet):
    queryset = Channel.objects.select_related("exercise").prefetch_related("members", "crisis_cells")
    serializer_class = ChannelSerializer


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer

    def get_queryset(self):
        return Message.objects.select_related("channel", "sender").prefetch_related("attachments")

    def perform_create(self, serializer):
        message = serializer.save(sender=self.request.user)
        audit("message.created", actor=self.request.user, resource=message, exercise=message.channel.exercise)
