from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Message
from django.views import View

from .models import ChatRoom, Message

class ChatView(LoginRequiredMixin, TemplateView):
    template_name="chat/chat.html"
    login_url="/accounts/login/"

    # def get_context_data(self, **kwargs):
    #     context =  super().get_context_data(**kwargs)
    #     context["messages"] = Message.objects.all().order_by('timestamp')
    #     return context
    
#to save it to db
class SendMessageView(LoginRequiredMixin,View):
    def post(self,request):
        content = request.POST.get("content")
        Message.objects.create(user=request.user,content=content)
        return redirect('chat')
    

class OpenChat(LoginRequiredMixin,View):
    def get(self, request,room_name):

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