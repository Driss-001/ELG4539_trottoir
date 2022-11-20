// Collecting data from IR sensors and a load cell
#include "HX711.h"
#include <Arduino.h> 
 
// HX711 circuit wiring
const int LOADCELL_DOUT_PIN = 8;
const int LOADCELL_SCK_PIN = 9;
int ir5IN = 6;
int ir4IN = 5; 
int ir3IN = 4; 
int ir2IN = 3; 
int ir1IN = 2; 
int pir1State = LOW;             // we start, assuming no motion detected
int pir2State = LOW;             // we start, assuming no motion detected
int pir3State = LOW;             // we start, assuming no motion detected
int pir4State = LOW;             // we start, assuming no motion detected
int val1 = 0;                    // variable for reading the pin status
int val2 = 0;                    // variable for reading the pin status
int val3 = 0;                    // variable for reading the pin status
int val4 = 0;                    // variable for reading the pin status
int val5 = 0;                    // variable for reading the pin status
 
int IRarray = 0;                    // variable for sending IR status to pi
 
HX711 scale; 
 
void setup() {
  pinMode(ir1IN, INPUT);      // 
  pinMode(ir2IN, INPUT);     // 
  pinMode(ir3IN, INPUT);
  pinMode(ir4IN, INPUT);
  pinMode(ir5IN, INPUT);
   
  Serial.begin(76800);
  
  scale.begin(LOADCELL_DOUT_PIN, LOADCELL_SCK_PIN);
  scale.set_scale(105.73399);
  scale.tare();               // reset the scale to 0
  
}
 
void loop(){
  val1 = digitalRead(ir1IN);  // read input value
  val2 = digitalRead(ir2IN);  // read input value
  val3 = digitalRead(ir3IN);  // read input value
  val4 = digitalRead(ir4IN);  // read input value
  val5 = digitalRead(ir5IN);  // read input value
 
  IRarray= val1 + 2*val2 + 4*val3 + 8*val4 + 16*val5;
  Serial.println(IRarray);
  Serial.println(scale.get_units(), 1);
  
delay(1);
  
  
}
