#!/usr/bin/python3
import math  as mt 
import random as rd
import serial , re ,time,sys ,threading ,serial.tools.list_ports
import time


ports = list(serial.tools.list_ports.comports())

for p in ports:
    print(p)
    if "ttyAMA0" in p.description:
        com1  = p.device


class Decision_master:

    def __init__(self,com):
        self.baudrate = 115200
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
            print('reading...')
            self.raw_data = ser.readline().decode(("ascii"))
            print(f"reading : {self.raw_data}")
            time.sleep(1e-3)

    def Reading_thread(self):
        self.th1 = threading.Thread(target = self.__serial_measurement)
        self.th1.daemon = True
        self.th1.start()
        for i in range(0,10):
            print(f"time is {i} s")
            time.sleep(1)
        self.reading = False
        
        #self.th1.join()
        

    #def __apply_decision(self):

if __name__ == "__main__":
    D1 = Decision_master(com1)
    D1.Reading_thread()
        


