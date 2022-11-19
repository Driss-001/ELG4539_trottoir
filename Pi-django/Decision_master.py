#!/usr/bin/python3
import math  as mt 
import random as rd
import serial , re ,time,sys ,threading ,serial.tools.list_ports
import time


ports = list(serial.tools.list_ports.comports())

for p in ports:
    if "ttyAMA0" in p.description:
        com1  =p.name

class Decision_master:

    def __init__(self,com):
        self.baudrate = 76800
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
        if self.com != None:
            ser = serial.serial(self.com)
            ser.baudrate = self.baudrate
            while self.reading:
                self.raw_data = ser.readline().decode(("ascii"))
                print(self.raw_data)
                time.sleep(1e-3)

    def Reading_thread(self):
        self.thread1 = threading.thread(target = self.__serial_measurement)
        self.thread1.daemon = True
        self.thread.start()
        time.sleep(5)
        self.reading = False
        self.thread1.join()
        

    #def __apply_decision(self):

if __name__ == "__main__":
    D1 = Decision_master(com1)
    D1.Reading_thread()


