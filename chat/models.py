from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Message(models.Model):
    sender = models.ForeignKey(User,on_delete=models.CASCADE) #need to use other than CASCADE, as message can be there even if user is deleted
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    chatroom = models.ForeignKey('ChatRoom',on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return f"{self.sender} : {self.content}"
    
class ChatRoom(models.Model):
    name = models.CharField(max_length=20)
    members = models.ManyToManyField(User,related_name="chats")
    is_group = models.BooleanField(default=True)
    is_private = models.BooleanField(default=False)
    creator = models.ForeignKey(User,null=True,on_delete=models.SET_NULL,related_name="groupscreated") #chat will exist even if admin deleted their account
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

