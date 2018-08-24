/*
  Blink
  Turns on an LED on for one second, then off for one second, repeatedly.
 
  This example code is in the public domain.
 */
 
// Pin 13 has an LED connected on most Arduino boards.
// give it a name:
int ledA = 0;
int ledB = 1;
int ledC = 2;
int ledD = 3;
int ledE = 4;
int ledF = 5;
int ledG = 6;
int ledH = 7;
int ledI = 8;
int ledJ = 9;
int ledK = 10;
int ledL = 11;
int delayTime = 100;

// the setup routine runs once when you press reset:
void setup() {                
  // initialize the digital pin as an output.
  pinMode(ledA, OUTPUT);
  pinMode(ledB, OUTPUT);
  pinMode(ledC, OUTPUT);
  pinMode(ledD, OUTPUT);
  pinMode(ledE, OUTPUT);
  pinMode(ledF, OUTPUT);
  pinMode(ledG, OUTPUT);
  pinMode(ledH, OUTPUT);
  pinMode(ledI, OUTPUT);
  pinMode(ledJ, OUTPUT);
  pinMode(ledK, OUTPUT);
  pinMode(ledL, OUTPUT);
}

// the loop routine runs over and over again forever:
void loop() {
  digitalWrite(ledA, HIGH);
  digitalWrite(ledG, HIGH);
  delay(delayTime);
  digitalWrite(ledA, LOW);
  digitalWrite(ledG, LOW);
  digitalWrite(ledB, HIGH);
  digitalWrite(ledH, HIGH);
  delay(delayTime);
  digitalWrite(ledB, LOW);
  digitalWrite(ledH, LOW);
  digitalWrite(ledC, HIGH);
  digitalWrite(ledI, HIGH);
  delay(delayTime);
  digitalWrite(ledC, LOW);
  digitalWrite(ledI, LOW);
  digitalWrite(ledD, HIGH);
  digitalWrite(ledJ, HIGH);
  delay(delayTime);
  digitalWrite(ledD, LOW);
  digitalWrite(ledJ, LOW);
  digitalWrite(ledE, HIGH);
  digitalWrite(ledK, HIGH);
  delay(delayTime);
  digitalWrite(ledE, LOW);
  digitalWrite(ledK, LOW);
  digitalWrite(ledF, HIGH);
  digitalWrite(ledL, HIGH);
  delay(delayTime);
  digitalWrite(ledF, LOW);
  digitalWrite(ledL, LOW);
}