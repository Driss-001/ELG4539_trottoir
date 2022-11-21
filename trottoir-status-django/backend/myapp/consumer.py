from channels.generic.websocket import AsyncJsonWebsocketConsumer


class RoadState(AsyncJsonWebsocketConsumer):
    async def connect(self):    

        print(self.scope)    
        await self.accept()  

    async def disconnect(self, close_code):

        await self.disconnect()

    async def receive(self, state_data = None, text_data = None):

        if text_data == 'PING':
                 await self.send('PONG')
        
        print(">>>>",state_data)
        pass       
