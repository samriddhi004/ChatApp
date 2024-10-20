from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Message,ChatRoom
from django.views import View
from django.contrib.auth.models import User

from .models import ChatRoom, Message

class ChatView(LoginRequiredMixin, TemplateView):
    template_name="chat/chat.html"
    login_url="/accounts/login/"
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["rooms"] = ChatRoom.objects.all()
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
        user = request.user
        chatfilter = ChatRoom.objects.filter(name=room_name)
        if chatfilter.exists():
            chat = chatfilter[0]
            if not user in chat.members.all():
                chat.members.add(user)

            #getting old messages
            messagesobj = Message.objects.filter(chatroom = chat)

            for msg in messagesobj:
                messages.append({'message':msg.content,
                                 'username':msg.sender.username,
                                 'timestamp':msg.timestamp.strftime('%H:%M:%S')})
            
        else:
            newchat = ChatRoom(name=room_name,creator=user)
            newchat.save()
            newchat.members.add(user)


        return render(request,"chat/room.html",{
            "room_name":room_name,
            "messages":messages
        })
        
class PrivateChatView(LoginRequiredMixin,View):
    login_url = "/accounts/login/"
    
    def get(self, request, username):
        
        friend = get_object_or_404(User,username=username)
        #if it exists
        pvt_chat = ChatRoom.objects.filter(is_private=True,is_group=False,members=request.user).filter(members=friend).first() #for querysets
        #create
        if not pvt_chat:
            pvt_chat = ChatRoom.objects.create(name=f"{friend.username}-{request.user.username}",is_private=True,is_group=False)  
            pvt_chat.members.add(request.user,friend)
        
        return render(request,"chat/room.html"),{
            "room_name" : pvt_chat.name,
            "messages":messages
            
        } )
        
           