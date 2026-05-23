from rest_framework import serializers

from messaging.models import Channel, DirectMessage, Message


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    sender_display = serializers.CharField(source="sender.get_full_name", read_only=True)

    class Meta:
        model = Message
        fields = "__all__"
        read_only_fields = ["sender", "created_at"]


class DirectMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectMessage
        fields = "__all__"
