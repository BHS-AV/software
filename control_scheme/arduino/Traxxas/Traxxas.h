// Benjamin S. Bussell
// February 26, 2019

#ifndef Traxxas_h
#define Traxxas_h

#include "Arduino.h"
#include <Servo.h>
#include <EEPROM.h>



class Traxxas {

private:

  Servo serv;
  int pin;
  int throttle;
  int delta;
  int value;
  int goal;

  bool angleBased = true;

public:

    Traxxas(int Pin, int Throttle, int Delta, int Value, int Goal):
        pin (Pin), throttle (Throttle), delta ( Delta), value ( Value), goal ( Goal){};
    ~Traxxas();
    void refresh();
    void startup();
    void executeArmingSequence();

    void setGoal(unsigned int argument);
    void setDelta(unsigned int value);

    unsigned int readPhysical();

    int loadServoValue();
    void storeServoValue();

};



#endif
