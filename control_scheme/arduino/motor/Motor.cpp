
// Benjamin S. Bussell
// February 26, 2019

#include "Arduino.h"
#include "Motor.h"
#include <Servo.h>

Motor::~Motor () {

}

void Motor::refresh() {
    // Smoothing with Deltas to prevent sudden increase
    int error = goal - value;
    int sign = abs(error) / error;

    if (error == 0 ) { return;}

    if (abs(error) > delta)
      value += delta*sign;
    else
      value = goal;

    
    serv.write(value);

}

void Motor::startup() {
    
    serv.attach(pin);
    
}



void Motor::setGoal( unsigned int argument) {
  // TODO: Implement Error Checking to prevent from inappropriate Arguments
  //       Ex: if argument is out of range of motors or something dumb.
  goal = argument;
}

void Motor::setDelta( unsigned int value) {

  delta = value;
  //Serial.print(delta);
}

int Motor::loadServoValue() {
    int val;
    for ( int address = 0; address < sizeof(int); address++)
      val = (val + EEPROM.read(address)) << 8;

    return val;
}

void Motor::storeServoValue() {
  for(int address = 0; address < sizeof(int); address++) {
    byte val = (value >> (8*(sizeof(int) - address - 1))) & 255;
    EEPROM.write(address, val);
  }
}

unsigned int Motor::readPhysical() {

  if (!angleBased)
    return serv.readMicroseconds();
  else
    return serv.read();

}