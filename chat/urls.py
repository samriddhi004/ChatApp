from django.urls import path
from .views import ChatView,SendMessageView
from . import views
urlpatterns=[
    path("",ChatView.as_view(),name="chat"),
    path("send_msg",SendMessageView.as_view(),name="send_msg"),
    path("<str:room_name>/",views.room,name="room"),
] 
