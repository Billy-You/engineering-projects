#include <Servo.h>

Servo myServo;

const int potPin = A0;
const int servoPin = 9;

int adcValue = 0;
int angle = 0;

void setup() {
  Serial.begin(9600);
  myServo.attach(servoPin);
}

void loop() {
  adcValue = analogRead(potPin);
  angle = map(adcValue, 0, 1023, 0, 180);

  myServo.write(angle);

  Serial.print("ADC: ");
  Serial.print(adcValue);
  Serial.print(" | Angle: ");
  Serial.println(angle);

  delay(20);
}