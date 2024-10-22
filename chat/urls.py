from django.urls import path
from .views import ChatView,SendMessageView
from . import views
urlpatterns=[
    path("",ChatView.as_view(),name="chat"),
    # path("send_msg",SendMessageView.as_view(),name="send_msg"),
    path("<str:room_name>/",views.OpenChat.as_view(),name="room"),
    path("dm/<str:room_name>/",views.PrivateChatView.as_view(),name="pvt_chat"),
    path("dm/<str:room_name>/options/",views.RoomOptionsView.as_view(),name='roomoptions')
] 
