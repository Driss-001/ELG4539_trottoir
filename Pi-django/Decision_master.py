import math  as mt 
import random as rd
import serial , re ,time,sys ,threading ,serial.tools.list_ports
import time


ports = list(serial.tools.list_ports.comports())

for p in ports:
    print(p)
    if "Silicon Labs" in p.description:
        com  =p.name

class Decision_master:

    def __init__(self,com1):
        self.baudrate = 76800
        self.sensors = com1
        #Constants
        #15cm between IR sensors
        self.delta_d = 15e-2
        #decision  lists for quick access
        self.lamp_modes = ["off","on"]
        road_states = ['None',"pedestrian","Car"]
        self.current_lamp_mode = self.lamp_modes[0]
        self.current_road_state = self.road_states[0]




    def __decision_randomizer(self):
        #mock random signal generator
        rand_lamp_mode = rd.randint(0,len(self.lamp_modes)-1)
        rand_road_state = rd.randint(0,len(self.road_states)-1)
        self.current_lamp_mode = self.lamp_modes[rand_lamp_mode]
        self.current_road_state = self.road_states[rand_road_state]

    
    #def __serial_measurement(self):


    #def __apply_decision(self):




