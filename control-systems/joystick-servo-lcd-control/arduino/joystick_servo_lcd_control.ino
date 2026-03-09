#include <Servo.h>

Servo myServo;

const int joyXPin = A0;
const int servoPin = 9;

int joyXValue = 0;
int angle = 0;

void setup() {
  Serial.begin(115200);
  myServo.attach(servoPin);

  Serial.println("Joystick + Servo control iniciado");
}

void loop() {
  joyXValue = analogRead(joyXPin);

  angle = map(joyXValue, 0, 1023, 0, 180);
  angle = constrain(angle, 0, 180);

  myServo.write(angle);

  Serial.print("JoyX: ");
  Serial.print(joyXValue);
  Serial.print(" | Angle: ");
  Serial.println(angle);

  delay(20);
}