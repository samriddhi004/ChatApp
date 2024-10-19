# from .models import ChatRoom,Message

# def get_chatroom_messages(room_name,is_private=False,is_group=True,members=None):
    
#     messages=[]
#     chat_room = ChatRoom.objects.filter(name=room_name,is_private=is_private,is_group=is_group)
    
#     if chat_room.exists():
#         chat_room = chat_room[0]
#     else:
#         chat_room = ChatRoom(name=room_name,is_private=is_private,is_group=is_group)
#         chat_room.save()
#         if members:
#             chat_room.members.add(*members)
            
#     msgss = Message.objects.filter(chatroom = chat_room)
#     for msg in msgss:
#         messages.append({
#             "message":msg.content,
#             "username":msg.sender
            
#         })
        