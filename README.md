# Chat App

A real-time chat application built with django channels and websockets.

## Setting Up
- git pull
- python manage.py makemigrations
- python manage.py migrate
- python manage.py create_superusers 
- sudo docker run -p 6379:6379 -d redis:5
- python manage.py runserver


(This command creates 10 dummy users for testing purpose
usernames: [rohit, sam, bikash, pallavi,..] and password is same as username)

## Have Done ✅

- created models for Message and ChatRoom
- creating a new chat room while someone opens a new room
- if an new user joins existing room, he/she is added as that chat member
- messages are saved while receiving them in consumers.py
- passing history message of correspoding chatroom as context to room.html (message persistancy)
- list down available chatrooms with option to join one of them in chat.html
- leave option added in chatroom
- "joined the room" and "left the room" message shown
- room options view added to get details about chatroom


## To Do 📝

### Sam
- Implement DM feature to available users by searching
- Adding more members while creating a new chatroom
- List down only room which you are member of
- You can search both room and individual through searching feature
- Let them chose room type while creating room (private or not)
- You cannot join private room by searching, either you need a invitation link or admin should add you.

### Rohit
- 'Add member'/'Remove member' feature in chatroom (Only admin can if it is private group)
- 
