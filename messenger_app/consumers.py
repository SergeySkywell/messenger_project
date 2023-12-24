# messenger_app/consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
from .models import Message

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.chat_id = self.scope['url_route']['kwargs']['chat_id']
        self.chat_group_name = f"group_chat_{self.chat_id}"

        # Join room group
        await self.channel_layer.group_add(
            self.chat_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.chat_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        message_data = json.loads(text_data)
        message_content = message_data['content']

        # Save message to the database
        message = Message.objects.create(
            sender=self.scope['user'].userprofile,
            content=message_content,
            chat_id=self.chat_id
        )

        # Send message to room group
        await self.channel_layer.group_send(
            self.chat_group_name,
            {
                'type': 'chat.message',
                'message': {
                    'id': message.id,
                    'sender': message.sender.id,
                    'content': message.content,
                    'timestamp': message.timestamp.isoformat(),
                }
            }
        )

    # Receive message from room group
    async def chat.message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
