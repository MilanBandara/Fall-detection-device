#include <ESP8266WiFi.h>
#include <WiFiUdp.h>
#include <MPU6050.h>
#include <Wire.h>

const char* ssid = "SLT-4G-74DDAD";
const char* password = "6ES2TFM472";
const char* server_address = "192.168.1.248";
const int server_port = 1234;

MPU6050 mpu;
WiFiUDP udp;

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
  Wire.begin();
  mpu.initialize();
  WiFi.begin(ssid, password);//connecting to the WiFi network
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
  }
}

void loop() {
  for(int i = 0; i < 10; i++) { // send 10 data points per loop iteration
    // Read sensor data
    int16_t ax, ay, az, gx, gy, gz;
    mpu.getAcceleration(&ax, &ay, &az);
    mpu.getRotation(&gx, &gy, &gz);

    // Send sensor data over UDP
    udp.beginPacket(server_address, server_port);
    udp.write((uint8_t*)&ax, sizeof(ax));
    udp.write((uint8_t*)&ay, sizeof(ay));
    udp.write((uint8_t*)&az, sizeof(az));
    udp.write((uint8_t*)&gx, sizeof(gx)); // send gyro data
    udp.write((uint8_t*)&gy, sizeof(gy));
    udp.write((uint8_t*)&gz, sizeof(gz));
    udp.endPacket();
    
    Serial.print("Data sent ");
    Serial.println(ax);
  }

  // You can also remove the delay, as it may cause some delay in data transmission
}
