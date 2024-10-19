# Chat App

A real-time chat application built with django channels and websockets.

## Setting Up

- python manage.py create_superusers 

(This command creates 10 dummy users for testing purpose
usernames: [rohit, sam, bikash, pallavi,..] and password is same as username)

## Have Done ✅

- created models for Message and ChatRoom
- creating a new chat room while someone opens a new room
- if an new user joins existing room, he/she is added as that chat member
- messages are saved while receiving them in consumers.py
- passing history message of correspoding chatroom as context to room.html (message persistancy)
- list down available chatrooms with option to join one of them in chat.html

## Following 

- https://channels.readthedocs.io/en/stable/tutorial/part_1.html

## To Do 📝

- Implement DM feature to available users by searching
- 
