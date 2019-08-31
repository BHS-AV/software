// Benjamin S. Bussell
// February 26, 2019

// If having trouble with the code submit an issue here:
// https://github.com/BSBussell/VESC


#include "Arduino.h"
#include <Servo.h>

#include <Motor.h>
// Custom Library made to abstract the code helping readability.
// Can be found in Motor folder
// If modified needs to be recompiled from Sketch > Include Library > Add .ZIP Library
// Might need to rename the folder, just add one version number to the name.




// Motor object(pin, throttle,delta, value, goal)
Motor Steering(9, 1, 1, 90, 90);




// For keeping track of updates
unsigned long time;
unsigned long prevTime;

// if you're new to arduino this code runs before the loop.
// Any setup needs to happen here
// I initalized variable above so that they are included in the Global scope
void setup() {

  

  
  // Initalize the motors.
  Steering.startup();


  // Initalize ports and make sure they are working, code will not run until they do
  Serial.begin(9600);
  
  while (!Serial) {
    ;
  }

}

// This loop called every 'frame'
// Main action
void loop() {

  // set the time
  time = millis();

  // Make sure time has passed since last loop, to prevent weird stacking issues
  if ( prevTime != time ) {
    
    Steering.refresh();
    prevTime = time;
  }

  // Check for inputs from python.
  if (Serial.available() > 2) {

    // Byte 1 - Instruction
    // Byte 2 - High Value
    // Byte 3 - Low Value
    // Read the IO Port
    
    char instruction = Serial.read();
    unsigned int argument = parseBytes(); // Parse Bytes reads the two bytes sent and merges them to a 16 bit int
    
    // 3/6/2019 - Added lower case for changing Delta with the Arduino
    
    switch(instruction) {
      case 'S':
        Steering.setGoal(argument);
        break;
      case 's':
        Steering.setDelta(argument);
         break;
      
    }

  }
  
  // Set finish time for use above.
  
}

int parseBytes() {
  
  byte high = Serial.read();
  byte low  = Serial.read();
  
  return high * 256 + low;
}
