import math  as mt 
import random as rd
import serial , re ,time,sys ,threading ,serial.tools.list_ports
import time



#decision  lists for quick access
lamp_modes = ["off","on"]
road_states = ['None',"pedestrian","Car"]


#mock random signal generator
rand_lamp_mode = rd.randint(0,len(lamp_modes)-1)
rand_road_state = rd.randint(0,len(road_states)-1)

current_lamp_mode = lamp_modes[rand_lamp_mode]
current_road_state = road_states[rand_road_state]



