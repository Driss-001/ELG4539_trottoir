import os
from channels.routing import ProtocolTypeRouter,URLRouter
from django.core.asgi import get_asgi_application
from django.urls import path
from myapp import consumer

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

websocket_urlPattern = [ 
    path('ws/RoadState',consumer.RoadState),
    path('ws/TimeSeries'),
]

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter([
        websocket_urlPattern
    # you can define all your routers here
        ])
})