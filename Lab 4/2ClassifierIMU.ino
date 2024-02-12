#include <ArduinoMqttClient.h>
#include <WiFiNINA.h>
#include "wifi_secret.h"
#include <Arduino_LSM6DS3.h>

///////please enter your sensitive data in the Secret tab/arduino_secrets.h
//char ssid[] = SECRET_SSID;        // your network SSID (name)
//char pass[] = SECRET_PASS;    // your network password (use for WPA, or use as key for WEP)

int count = 0;

void setup() {
  //Initialize serial and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }
  
  if (!IMU.begin()) {
    Serial.println("Failed to initialize IMU!");

    while (1);
  }

  Serial.println();
}

void loop() {
  float ax, ay, az;
  float gx, gy, gz;  

  // save the last time a message was sent
  if (IMU.accelerationAvailable()) {
    IMU.readAcceleration(ax, ay, az);
    Serial.println();
    Serial.print("ax: ");
    Serial.print(ax);
    Serial.print("\t");
    Serial.print("ay: ");
    Serial.print(ay);
    Serial.print("\t");
    Serial.print("az: ");
    Serial.println(az);

    if (abs(ax) <= 0.15 && abs(ay) <= 0.1 && abs(az) - 1 <= 0.1) {
      Serial.println("Idle");
    }
    else if (az <= 0.8) {
      Serial.println("Upward Lift");
    }
    else if (ax > 0.15) {
      Serial.println("Forward Push");
    }
  }
}