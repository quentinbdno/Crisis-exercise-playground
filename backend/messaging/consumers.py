import json

from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

from messaging.models import Channel, Message


class ExerciseConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.exercise_id = self.scope["url_route"]["kwargs"]["exercise_id"]
        self.group_name = f"exercise_{self.exercise_id}"
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        payload = json.loads(text_data)
        if payload.get("type") == "message":
            message = await self.create_message(payload)
            await self.channel_layer.group_send(
                self.group_name,
                {
                    "type": "exercise.message",
                    "message": {
                        "id": message.id,
                        "channel": message.channel_id,
                        "body": message.body,
                        "sender": message.sender_id,
                        "created_at": message.created_at.isoformat(),
                    },
                },
            )

    async def exercise_message(self, event):
        await self.send(text_data=json.dumps(event["message"]))

    @sync_to_async
    def create_message(self, payload):
        channel = Channel.objects.get(pk=payload["channel_id"], exercise_id=self.exercise_id)
        user = self.scope.get("user")
        return Message.objects.create(channel=channel, sender=user if user and user.is_authenticated else None, body=payload["body"])
