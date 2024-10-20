import json
# from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Message, ChatRoom
from channels.db import database_sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s"%self.room_name
        self.chat_room = await self.get_chat_room()
        self.username = self.scope['user'].username 

        await (self.channel_layer.group_add)(self.room_group_name, self.channel_name)
        
        await self.accept()

        await self.channel_layer.group_send(
                    self.room_group_name,
                    {"type": "chat_message",
                    "controlsignal" : "joinroom",
                    "message" : "joined the room",
                    "username":self.username,
                    "timestamp":"" 
                    }
                )
        
        
    
    #for async database query operation
    @database_sync_to_async
    def get_chat_room(self):
        room_name = self.room_name
        user = self.scope['user']
        room = ChatRoom.objects.get(name=self.room_name)
        if not room.is_private or (room.is_private and user in room.members.all()):
            return room
        else:
            return None

    @database_sync_to_async
    def save_message(self,message):
        return Message.objects.create(sender=self.scope['user'],content=message,chatroom=self.chat_room)

    @database_sync_to_async
    def remove_from_room(self):
        return self.chat_room.members.remove(self.scope['user'])

    async def disconnect(self, close_code):
        await (self.channel_layer.group_discard)(
            self.room_group_name,self.channel_name #user no longer part of chatroom
        )
    
    async def receive(self,text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        

        controlsignal = text_data_json["controlsignal"]
        if controlsignal == True:
            if message == "leaveroom":
                await self.remove_from_room()

                await self.channel_layer.group_send(
                    self.room_group_name,
                    {"type": "chat_message",
                    "controlsignal" : "leaveroom",
                    "message" : "left the room",
                    "username":self.username,
                    "timestamp":"" 
                    }
                )
                await self.disconnect(1000)

        else:

            newmsgobj = await self.save_message(message)
            timestamp = newmsgobj.timestamp.strftime('%H:%M:%S')

            await self.channel_layer.group_send(
                self.room_group_name,
                {"type": "chat_message",
                "controlsignal" : "textmessage",
                "message" : message,
                "username":self.username,
                "timestamp":timestamp
                }
            )
        

    async def chat_message(self,event):
        controlsignal = event["controlsignal"]
        message = event["message"]
        username = event["username"]
        timestamp = event["timestamp"]

        await self.send(text_data=json.dumps({"controlsignal":controlsignal,"message":message,"username":username,"timestamp":timestamp}))
        
        