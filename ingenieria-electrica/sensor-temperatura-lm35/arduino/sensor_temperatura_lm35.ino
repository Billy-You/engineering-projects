const int sensorPin = A0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int adc = analogRead(sensorPin);
  float voltaje = (adc * 5.0) / 1023.0;
  float temperatura = voltaje * 100.0;

  Serial.print("ADC: ");
  Serial.print(adc);
  Serial.print(" | Vout: ");
  Serial.print(voltaje, 4);
  Serial.print(" V | Temp: ");
  Serial.print(temperatura, 2);
  Serial.println(" C");

  delay(1000);
}

