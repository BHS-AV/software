
// Benjamin S. Bussell
// February 26, 2019

#include "Arduino.h"
#include "Traxxas.h"
#include <Servo.h>

Traxxas::~Traxxas () {

}

void Traxxas::refresh() {
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

void Traxxas::startup() {

    serv.write(90);
    serv.attach(pin);
}



void Traxxas::setGoal( unsigned int argument) {
  // TODO: Implement Error Checking to prevent from inappropriate Arguments
  //       Ex: if argument is out of range of Traxxass or something dumb.
  goal = argument;
}

void Traxxas::setDelta( unsigned int value) {

  delta = value;
  //Serial.print(delta);
}

int Traxxas::loadServoValue() {
    int val;
    for ( int address = 0; address < sizeof(int); address++)
      val = (val + EEPROM.read(address)) << 8;

    return val;
}

void Traxxas::storeServoValue() {
  for(int address = 0; address < sizeof(int); address++) {
    byte val = (value >> (8*(sizeof(int) - address - 1))) & 255;
    EEPROM.write(address, val);
  }
}

unsigned int Traxxas::readPhysical() {

  if (!angleBased)
    return serv.readMicroseconds();
  else
    return serv.read();

}
