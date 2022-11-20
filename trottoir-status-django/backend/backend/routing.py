from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from myapp import consumer


websocket_urlPattern = [ 
    path('ws/RoadState',consumer.RoadState),
    path('ws/TimeSeries'),
]

application = ProtocolTypeRouter({
    'websocket':AuthMiddlewareStack(URLRouter(websocket_urlPattern))

})
