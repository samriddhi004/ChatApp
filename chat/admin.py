from django.contrib import admin
from .models import Message, ChatRoom
# Register your models here.

# class MessageAdmin(admin.ModelAdmin):
#     list_display=("user","content","timestamp")
    
# admin.site.register(Message,MessageAdmin)

admin.site.register(ChatRoom)