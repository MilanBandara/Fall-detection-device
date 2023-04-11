#include <Wire.h>
#include <MPU6050.h>

MPU6050 mpu;

void setup() {
  Serial.begin(9600);
  Wire.begin();
  mpu.initialize();
}

void loop() {
  int16_t ax, ay, az;
  int16_t gx, gy, gz;
  mpu.getAcceleration(&ax, &ay, &az);
  mpu.getRotation(&gx, &gy, &gz);
  Serial.print("Ax: ");
  Serial.print(ax);
  Serial.print(", Ay: ");
  Serial.print(ay);
  Serial.print(", Az: ");
  Serial.print(az);
  Serial.print(", Gx: ");
  Serial.print(gx);
  Serial.print(", Gy: ");
  Serial.print(gy);
  Serial.print(", Gz: ");
  Serial.println(gz);
}
