
import math  as mt 
import random as rd
import numpy as np
import serial , re ,time,sys ,threading ,serial.tools.list_ports
import json


ports = list(serial.tools.list_ports.comports())

for p in ports:
    print(p)
    if "ttyAMA0"  or "CH340" in p.description:
        com1  = p.device

ball_weight = 195/4

class Decision_master:

    def __init__(self,com,time = 1):
        self.time = time
        self.baudrate = 19200
        self.com = com
        #Constants
        #15cm between IR sensors
        self.reading = True
        self.delta_d = 15e-2
        #decision  lists for quick access
        self.lamp_modes = ["off","on"]
        self.road_states = ['None',"pedestrian","Car","Vélo"]
        #Initialisation
        self.current_lamp_mode = self.lamp_modes[0]
        self.current_road_state = self.road_states[0]
        self.current_speed = 0
        self.current_weight = 0
        self.current_i = 0
        self.previous_i = 0
        self.previous_time = 0



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
            #print(f"raw data:{raw_data} \n processed data : {self.data}")
            #print(f"first Ir sensor : {Ir_position[0]} ,second Ir sensor: {Ir_position[1]} ")
            self.current_i, self.current_j = Ir_position
            self.current_time = time.time()
            self.current_weight = self.data[1]
            
            time.sleep(2e-3)
            self.current_speed = self._Speed_Eval()
            if self.current_speed!=0:
                self.previous_i = self.current_i
                self.previous_time = self.current_time

    def Reading_thread(self):
        self.th1 = threading.Thread(target = self.__serial_measurement)
        self.th2 = threading.Thread(target = self._Set_State)
        self.th1.daemon = True
        self.th2.daemon = True
        self.th1.start()
        self.th2.start()
        for i in range(0,round(60*self.time)):
            print(f"current_position: {self.current_i} current speed is {self.current_speed} m/s, current weight is {self.current_weight}g")
            time.sleep(1)
        self.reading = False    
        
        #self.th1.join()


    def _Ir_process(self,Ir_int):

        pos = lambda x: mt.log2(x)
        if Ir_int>=1:
            i = mt.trunc(pos(Ir_int))+1
        else:
            i=0
        if (Ir_int-2**i)<1:
            j = 0
        else:
            j=mt.trunc(pos(Ir_int-2**i))+1    

        return np.array([i,j])    

    def _Speed_Eval(self):
        if self.current_i > self.previous_i:
            v = self.delta_d*abs(self.current_i-self.previous_i)/(self.current_time-self.previous_time)
            self.current_i = 0
        else:
            v=0
        return v        
        
    def _Set_State(self):
        while self.reading:
            if self.current_speed > 0:
                if self.current_weight>0:
                    self.current_lamp_mode = self.lamp_modes[1]
                    self.current_road_state = self.road_states[1]
                    if self.current_time > 100:
                        self.current_road_state = self.road_states[3]
                        if self.current_road_state>150:
                            self.current_road_state = self.road_states[2]
                            self._tojson()
                time.sleep(10)            
            else:
                self.current_lamp_mode = self.lamp_modes[0]
                self.current_road_state = self.road_states[0]
                self._tojson()
                                

    def _tojson(self):

        dictionary = {
            "RoadState": self.current_road_state,
            "LampState": self.current_lamp_mode,
    
                    }

        json_object = json.dumps(dictionary, indent=4)

        with open("state.json", "w") as outfile:
            outfile.write(json_object)
            
    #def __apply_decision(self):

if __name__ == "__main__":
    D1 = Decision_master(com1,time=5)
    D1.Reading_thread()
        


