# messenger_project/routing.py

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import re_path
from messenger_app.consumers import ChatConsumer

application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter(
            [
                re_path(r"ws/chat/(?P<chat_id>\w+)/$", ChatConsumer.as_asgi()),
            ]
        )
    ),
})
