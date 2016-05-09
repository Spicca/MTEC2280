#include "LedControl.h"
LedControl lc=LedControl(12,11,10);  // Pins: DIN,CLK,CS, # of Display connected

unsigned long delayTime=200;  // Delay between Frames



int sensorValue = 0;
int multiValue = 0;
int highR=1023;
int lowR=0;
int mapped = 0;
int ledPin8 = 7;
int ledPin7 = 6;
int ledPin6 = 5;
boolean check = true;
boolean check1 = true;
boolean check2 = true;
boolean check3 = true;
boolean check4 = true;


byte invader1a[] =
{
   B00011000,  // First frame of invader #1
   B00111100,
   B01111110,
   B11011011,
   B11111111,
   B00100100,
   B01011010,
   B10100101
};

byte invader1b[] =
{
  B00011000, // Second frame of invader #1
  B00111100,
  B01111110,
  B11011011,
  B11111111,
  B00100100,
  B01011010,
  B01000010
};

byte invader2a[] =
{
  B00100100, // First frame of invader #2
  B00100100,
  B01111110,
  B11011011,
  B11111111,
  B11111111,
  B10100101,
  B00100100
};

byte invader2b[] =
{
  B00100100, // Second frame of invader #2
  B10100101,
  B11111111,
  B11011011,
  B11111111,
  B01111110,
  B00100100,
  B01000010
};

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(ledPin6, OUTPUT);
pinMode(ledPin7, OUTPUT);
pinMode(ledPin8, OUTPUT);

  lc.shutdown(0,false);  // Wake up displays
  lc.shutdown(1,false);
  lc.setIntensity(0,5);  // Set intensity levels
  lc.setIntensity(1,5);
  lc.clearDisplay(0);  // Clear Displays
  lc.clearDisplay(1);
}


//  Take values in Arrays and Display them
void sinvader1a()
{
  for (int i = 0; i < 8; i++)  
  {
    lc.setRow(0,i,invader1a[i]);
  }
}

void sinvader1b()
{
  for (int i = 0; i < 8; i++)
  {
    lc.setRow(0,i,invader1b[i]);
  }
}

void loop() {
{
// Put #1 frame on both Display
    sinvader1a();
    delay(delayTime);
}


if(multiValue>=60){
    digitalWrite(ledPin6, LOW);
  digitalWrite(ledPin7, LOW);
  digitalWrite(ledPin8, LOW);
}
else if((multiValue<60) && (multiValue>=50)){
  digitalWrite(ledPin6, LOW);
  digitalWrite(ledPin7, LOW);
  digitalWrite(ledPin8, HIGH);
}
else if((multiValue<50) && (multiValue>=40)){
  digitalWrite(ledPin6, LOW);
  digitalWrite(ledPin7, HIGH);
  digitalWrite(ledPin8, LOW);
}
else if((multiValue<40) && (multiValue>=30)){
  digitalWrite(ledPin6, HIGH);
  digitalWrite(ledPin7, LOW);
  digitalWrite(ledPin8, LOW);

}
else
{
  digitalWrite(ledPin6, HIGH);
  digitalWrite(ledPin7, HIGH);
  digitalWrite(ledPin8, HIGH);
}

  multiValue= analogRead(A1);
if(multiValue<40 && multiValue>=30 && check==true)
{
   Serial.println("Complete 1");
   check = false;
}

if(Serial.write() = "0"){
  check=true;
  check1=true;
  check2=true;
  check3=true;
  check4=true;
}



  //mapped = map(sensorValue, highR, lowR, 0, 255);
  //analogWrite(ledPin, mapped);

}
