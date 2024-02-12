#include <ArduinoMqttClient.h>
#include <WiFiNINA.h>
#include "wifi_secret.h"
#include <Arduino_LSM6DS3.h>

///////please enter your sensitive data in the Secret tab/arduino_secrets.h
//char ssid[] = SECRET_SSID;        // your network SSID (name)
//char pass[] = SECRET_PASS;    // your network password (use for WPA, or use as key for WEP)

WiFiClient wifiClient;
MqttClient mqttClient(wifiClient);

const char broker[] = "mqtt.eclipseprojects.io";
int port = 1883;
const char topic[]  = "ece180d/test";

//set interval for sending messages (milliseconds)
const long interval = 8000;
unsigned long previousMillis = 0;

int count = 0;

void setup() {
  //Initialize serial and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

  // attempt to connect to Wifi network:
  Serial.print("Attempting to connect to WPA SSID: ");
  Serial.println(ssid);
  while (WiFi.begin(ssid, pass) != WL_CONNECTED) {
    // failed, retry
    Serial.print(".");
    delay(5000);
  }

  Serial.println("You're connected to the network");
  Serial.println();

  Serial.print("Attempting to connect to the MQTT broker: ");
  Serial.println(broker);

  if (!mqttClient.connect(broker, port)) {
    Serial.print("MQTT connection failed! Error code = ");
    Serial.println(mqttClient.connectError());

    while (1);
  }

  Serial.println("You're connected to the MQTT broker!");
  
  if (!IMU.begin()) {
    Serial.println("Failed to initialize IMU!");

    while (1);
  }

  Serial.println();
}

void loop() {
  // call poll() regularly to allow the library to send MQTT keep alive which
  // avoids being disconnected by the broker
  mqttClient.poll();

  float ax, ay, az;
  float gx, gy, gz;  
  unsigned long currentMillis = millis();

  if (currentMillis - previousMillis >= interval) {
    // save the last time a message was sent
    previousMillis = currentMillis;
    if (IMU.accelerationAvailable()) {
      IMU.readAcceleration(ax, ay, az);
      Serial.print("Sending message to topic: ");
      Serial.println(topic);
      Serial.println();
      Serial.print("ax: ");
      Serial.print(ax);
      Serial.print("\t");
      Serial.print("ay: ");
      Serial.print(ay);
      Serial.print("\t");
      Serial.print("az: ");
      Serial.println(az);

      // send message, the Print interface can be used to set the message contents
      mqttClient.beginMessage(topic);
      mqttClient.print(ax);
      mqttClient.print("ax: ");
      mqttClient.print(ax);
      mqttClient.print("\t");
      mqttClient.print("ay: ");
      mqttClient.print(ay);
      mqttClient.print("\t");
      mqttClient.print("az: ");
      mqttClient.println(az);
      mqttClient.endMessage();
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

      // send message, the Print interface can be used to set the message contents
      mqttClient.beginMessage(topic);
      mqttClient.print(gx);
      mqttClient.print("gx: ");
      mqttClient.print(gx);
      mqttClient.print("\t");
      mqttClient.print("gy: ");
      mqttClient.print(gy);
      mqttClient.print("\t");
      mqttClient.print("gz: ");
      mqttClient.println(gz);
      mqttClient.endMessage();
    }
  }
}