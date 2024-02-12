/*
  Arduino LSM6DS3 - Simple Gyroscope

  This example reads the gyroscope values from the LSM6DS3
  sensor and continuously prints them to the Serial Monitor
  or Serial Plotter.

  The circuit:
  - Arduino Uno WiFi Rev 2 or Arduino Nano 33 IoT

  created 10 Jul 2019
  by Riccardo Rizzo

  This example code is in the public domain.
*/

#include <Arduino_LSM6DS3.h>

void setup() {
  Serial.begin(9600);
  while (!Serial);

  if (!IMU.begin()) {
    Serial.println("Failed to initialize IMU!");

    while (1);
  }

  Serial.print("Gyroscope sample rate = ");
  Serial.print(IMU.gyroscopeSampleRate());
  Serial.println(" Hz");
  Serial.println();
  Serial.println("Gyroscope in degrees/second");
  Serial.println("X\tY\tZ");
}

void loop() {
  float ax, ay, az;
  float gx, gy, gz;
  
  if (IMU.accelerationAvailable()) {
    IMU.readAcceleration(ax, ay, az);
    
    Serial.print("ax: ");
    Serial.print(ax);
    Serial.print("\t");
    Serial.print("ay: ");
    Serial.print(ay);
    Serial.print("\t");
    Serial.print("az: ");
    Serial.println(az);
  }
  
  if (IMU.gyroscopeAvailable()) {
    IMU.readGyroscope(gx, gy, gz);

    Serial.print("gx: ");
    Serial.print(gx);
    Serial.print("\t");
    Serial.print("gy: ");
    Serial.print(gy);
    Serial.print("\t");
    Serial.print("gz: ");
    Serial.println(gz);
  }
}