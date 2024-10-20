from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Message,ChatRoom
from django.views import View
from django.contrib.auth.models import User
from .utils import get_chatroom_messages
from .models import ChatRoom, Message

class ChatView(LoginRequiredMixin, TemplateView):
    template_name="chat/chat.html"
    login_url="/accounts/login/"
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        user = self.request.user
        group_chats = ChatRoom.objects.filter(is_group=True,members=user)
        pvt_chats = ChatRoom.objects.filter(is_private=True,members=user)
        pvt_chat_list = []
        for room in pvt_chats:
            friend = room.members.exclude(username=user.username).first()
            if friend:
                pvt_chat_list.append({"room_name":room.name,"friend":friend.username})
        context["group_chats"] = group_chats
        context["pvt_chats"] = pvt_chats
        return context
    
#to save it to db
class SendMessageView(LoginRequiredMixin,View):
    def post(self,request):
        content = request.POST.get("content")
        Message.objects.create(user=request.user,content=content)
        return redirect('chat')
    

class OpenChat(LoginRequiredMixin,View):
    def get(self,request,room_name):

        messages = []
        #group validation and updating
        # user = request.user
        # chatfilter = ChatRoom.objects.filter(name=room_name)
        # if chatfilter.exists():
        #     chat = chatfilter[0]
        #     if not user in chat.members.all():
        #         chat.members.add(user)

        #     #getting old messages
        #     messagesobj = Message.objects.filter(chatroom = chat)

        #     for msg in messagesobj:
        #         messages.append({'message':msg.content,
        #                          'username':msg.sender.username,
        #                          'timestamp':msg.timestamp.strftime('%H:%M:%S')})
            
        # else:
        #     newchat = ChatRoom(name=room_name,creator=user)
        #     newchat.save()
        #     newchat.members.add(user)
        chat,messages = get_chatroom_messages(room_name=room_name,is_group=True,is_private=False,members=[request.user])


        return render(request,"chat/room.html",{
            "room_name":room_name,
            "messages":messages
        })
        
class PrivateChatView(LoginRequiredMixin,View):
    login_url = "/accounts/login/"
    
    def get(self, request, username):
        
        friend = get_object_or_404(User,username=username)
        #if it exists
        room_name = f"{friend.username}"
        chat,messages = get_chatroom_messages(room_name=room_name,is_group=False,is_private=True,members=[request.user,friend])
        
        return render(request,"chat/room.html"),{
            "room_name" : pvt_chat.name,
            "messages":messages
            })
        
           