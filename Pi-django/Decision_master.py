
import math  as mt 
import random as rd
import numpy as np
import serial , re ,time,sys ,threading ,serial.tools.list_ports
import time


ports = list(serial.tools.list_ports.comports())

for p in ports:
    print(p)
    if "ttyAMA0"  or "CH340" in p.description:
        com1  = p.device


class Decision_master:

    def __init__(self,com):
        self.baudrate = 19200
        self.com = com
        #Constants
        #15cm between IR sensors
        self.reading = True
        self.delta_d = 15e-2
        #decision  lists for quick access
        self.lamp_modes = ["off","on"]
        self.road_states = ['None',"pedestrian","Car"]
        self.current_lamp_mode = self.lamp_modes[0]
        self.current_road_state = self.road_states[0]




    def __decision_randomizer(self):
        #mock random signal generator
        rand_lamp_mode = rd.randint(0,len(self.lamp_modes)-1)
        rand_road_state = rd.randint(0,len(self.road_states)-1)
        self.current_lamp_mode = self.lamp_modes[rand_lamp_mode]
        self.current_road_state = self.road_states[rand_road_state]

    
    def __serial_measurement(self):
        
        ser = serial.Serial(self.com)
        ser.baudrate = self.baudrate
        while self.reading == True:
            #print('reading...')
            raw_data = ser.readline().decode("ascii")
            self.data= [float(val) for val in raw_data.split(';')]
            self.data = np.array(self.data)
            Ir_position =self._Ir_process(self.data[0])
            print(f"raw data:{raw_data} \n processed data : {self.data}")
            print(f"first Ir sensor : {Ir_position[0]} ,second Ir sensor: {Ir_position[1]} ")
            time.sleep(1000e-3)

    def Reading_thread(self):
        self.th1 = threading.Thread(target = self.__serial_measurement)
        self.th1.daemon = True
        self.th1.start()
        for i in range(0,60):
            #print(f"time is {i} s")
            time.sleep(1)
        self.reading = False
        
        #self.th1.join()
        

    def _Ir_process(self,Ir_int):

        pos = lambda x: mt.log2(x)
        if Ir_int>1:
            i = mt.trunc(pos(Ir_int))
        else:
            i=0
        if (Ir_int-2**i)<1:
            j = 0
        else:
            j=mt.trunc(pos(Ir_int-2**i))

        return np.array([i,j])    

    #def __apply_decision(self):

if __name__ == "__main__":
    D1 = Decision_master(com1)
    D1.Reading_thread()
        


