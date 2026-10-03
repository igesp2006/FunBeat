#include <Arduino.h>


const int buttonPins[] = {3, 4, 5, 6, 7};
const int numButtons = sizeof(buttonPins) / sizeof(buttonPins[0]);

bool buttonStates[5] = {HIGH, HIGH, HIGH, HIGH, HIGH};

void setup()
{
  Serial.begin(9600);

  for (int i = 0; i < numButtons; i++)
  {
    pinMode(buttonPins[i], INPUT_PULLUP);
  }

  Serial.println("Arduino Nano button deck ready.");
}

void loop()
{
  for (int i = 0; i < numButtons; i++)
  {
    bool currentState = digitalRead(buttonPins[i]);

    
    if (buttonStates[i] == HIGH && currentState == LOW)
    {
      
      Serial.println(i + 1);
    }

    buttonStates[i] = currentState;
  }

  delay(50); 
}