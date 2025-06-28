import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .nlp import get_bot_response

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        response = get_bot_response(message)

        await self.send(text_data=json.dumps({
            'message': response
        }))

