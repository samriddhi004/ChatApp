from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Message
from django.views import View
# Create your views here.
class ChatView(LoginRequiredMixin, TemplateView):
    template_name="chat/chat.html"
    login_url="/accounts/login/"
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["messages"] = Message.objects.all().order_by('timestamp')
        return context
    
#to save it to db
class SendMessageView(LoginRequiredMixin,View):
    def post(self,request):
        content = request.POST.get("content")
        Message.objects.create(user=request.user,content=content)
        return redirect('chat')
    
def room(request,room_name):
    return render(request,"chat/room.html",{
        "room_name":room_name
    })