// Collecting data from IR sensors and a load cell
#include <Arduino.h>
#include "HX711.h"
#define SIZE_OF_ARRAY 2

//size of array to send
float data[SIZE_OF_ARRAY] ;
byte *p = (byte*)data;

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

void send_array(float msg[]) {
  

  for (int i=0;i<SIZE_OF_ARRAY;i++){
    //snprintf (buff, sizeof(buff), "%f", data[i]);
    Serial.print(msg[i]);
    if(i!=SIZE_OF_ARRAY-1){
      Serial.print(';');
      }
    }
  Serial.print('\n');
}
  
void setup() {
  Serial.begin(76800);
  Serial.flush();
  pinMode(ir1IN, INPUT);      // 
  pinMode(ir2IN, INPUT);     // 
  pinMode(ir3IN, INPUT);
  pinMode(ir4IN, INPUT);
  pinMode(ir5IN, INPUT);
  
  scale.begin(LOADCELL_DOUT_PIN, LOADCELL_SCK_PIN);
  scale.set_scale(103.0913705583756);
  scale.tare();               // reset the scale to 0

  // put your setup code here, to run once:
}

void loop() {
  val1 = digitalRead(ir1IN);  // read input value
  val2 = digitalRead(ir2IN);  // read input value
  val3 = digitalRead(ir3IN);  // read input value
  val4 = digitalRead(ir4IN);  // read input value
  val5 = digitalRead(ir5IN);  // read input value
 
  uint8_t IRarray= val1 + 2*val2 + 4*val3 + 8*val4 + 16*val5;
  data[0] = IRarray;
  data[1] = scale.get_units();
  //Serial.println(data[0]);
  //Serial.println(data[2]);;
  send_array(data);
  delay(1);
  Serial.flush();
  // put your main code here, to run repeatedly:
}