# Chat App

A real-time chat application built with django channels and websockets.

## Setting Up

- python manage.py create_superusers 

(This command creates 10 dummy users for testing purpose
usernames: [rohit, sam, bikash, pallavi,..] and password is same as username)

## Have Done ✅

- Implemented https://channels.readthedocs.io/en/stable/installation.html
- added gitignore
- added danphe app in settings.py INSTALLED_APPS
- modified asgi.py to use ProtocolTypeRouter
- added ASGI_APPLICATION = "chatapp.asgi.application" in settings.py
-

## Following 

- https://channels.readthedocs.io/en/stable/tutorial/part_1.html

## To Do 📝

-