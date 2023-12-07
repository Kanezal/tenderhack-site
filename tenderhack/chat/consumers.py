import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Chat, Message
from django.contrib.auth.models import User

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_id = self.scope['url_route']['kwargs']['room_id']
        self.room_group_name = 'chat_%s' % self.room_id

        # Check if the user is part of the chat
        user = self.scope["user"]
        if not await self.is_user_in_chat(user, self.room_id):
            await self.close()
            return

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Save the message to the database
        await self.save_message(self.scope["user"], message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
            }
        )

    async def chat_message(self, event):
        message = event['message']

        await self.send(text_data=json.dumps({
            'sender': self.scope["user"].username,
            'message': message
        }))

    @database_sync_to_async
    def save_message(self, user, message):
        chat = Chat.objects.get(id=self.room_id)
        Message.objects.create(chat=chat, sender=user, text=message)

    @database_sync_to_async
    def is_user_in_chat(self, user, room_id):
        chat = Chat.objects.get(id=room_id)
        return chat.performer == user or chat.customer == user