from channels.generic.websocket import AsyncJsonWebsocketConsumer


class TrottoirState(AsyncJsonWebsocketConsumer):
    
    async def connect(self):    
        self.groupname='Roadstate'
        await self.channel_layer.group_add(
            self.groupname,
            self.channel_name,
        )   
        await self.accept()  

    async def disconnect(self, close_code):

       await self.websocket_disconnect(
            self.groupname,
            self.channel_name
        )

    async def receive(self, state_data,**kwargs):

        data = self.decode_json(state_data)
        RoadState = data["RoadState"]
        LampState = data["LampState"]
        
        await self.send_json(
            {
                'type':'deprocessing',
                'RoadState': RoadState,
                'LampState': LampState
            }
        )

        print(">>>>",state_data)
        pass   
    
     