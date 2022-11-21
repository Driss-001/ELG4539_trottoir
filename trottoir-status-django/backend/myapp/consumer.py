from channels.generic.websocket import AsyncWebsocketConsumer
import json


class RoadState(AsyncWebsocketConsumer):
    async def connect(self):    

        print(self.scope)    
        await self.connect()   

    async def disconnect(self, close_code):

        await self.disconnect()

    async def receive(self, state_data):
        
        print(">>>>",state_data)
        pass       
