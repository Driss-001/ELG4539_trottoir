import math  as mt 
import serial , re ,time,sys ,threading ,serial.tools.list_ports



#decision  dictionnaries
lamp_modes = {"off":0,"on":1}
road_states = {"None":0,"pedestrian":1,"Car":2}
