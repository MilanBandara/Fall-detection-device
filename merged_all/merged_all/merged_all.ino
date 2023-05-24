#include <Wire.h>
#include <SoftwareSerial.h>
#include "MAX30105.h"
#include <MPU6050.h>
#include "heartRate.h"

MAX30105 particleSensor;
MPU6050 mpu;

#define rxPin D5
#define txPin D6
SoftwareSerial mySerial(rxPin,txPin);

const byte RATE_SIZE = 4; //Increase this for more averaging. 4 is good.
byte rates[RATE_SIZE]; //Array of heart rates
byte rateSpot = 0;
long lastBeat = 0; //Time at which the last beat occurred

float beatsPerMinute;
int beatAvg;

void setup()
{
  Serial.begin(9600);
  Serial.println("Initializing...");
  Wire.begin();
  mpu.initialize();

  // // SIM module
  // mySerial.begin(9600);
  // Serial.println("Initializing..."); 
  // delay(1000);

  // mySerial.println("AT"); //Once the handshake test is successful, it will back to OK
  // updateSerial();

  // Initialize sensor
  if (!particleSensor.begin(Wire, I2C_SPEED_FAST)) //Use default I2C port, 400kHz speed
  {
    Serial.println("MAX30105 was not found. Please check wiring/power. ");
    while (1);
  }
  Serial.println("Place your index finger on the sensor with steady pressure.");

  particleSensor.setup(); //Configure sensor with default settings
  particleSensor.setPulseAmplitudeRed(0x0A); //Turn Red LED to low to indicate sensor is running
  particleSensor.setPulseAmplitudeGreen(0); //Turn off Green LED

}

void loop()
{
  int16_t ax, ay, az;
  int16_t gx, gy, gz;
  long irValue = particleSensor.getIR();

  if (checkForBeat(irValue) == true)
  {
    //We sensed a beat!
    long delta = millis() - lastBeat;
    lastBeat = millis();

    beatsPerMinute = 60 / (delta / 1000.0);

    if (beatsPerMinute < 255 && beatsPerMinute > 20)
    {
      rates[rateSpot++] = (byte)beatsPerMinute; //Store this reading in the array
      rateSpot %= RATE_SIZE; //Wrap variable

      //Take average of readings
      beatAvg = 0;
      for (byte x = 0 ; x < RATE_SIZE ; x++)
        beatAvg += rates[x];
      beatAvg /= RATE_SIZE;
    }
  }

  Serial.print("IR=");
  Serial.print(irValue);
  Serial.print(", BPM=");
  Serial.print(beatsPerMinute);
  Serial.print(", Avg BPM=");
  Serial.print(beatAvg);

  if (irValue < 50000)
    Serial.print(" No finger?");
  Serial.println();
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

  if (az>10000){
    call2();
  }

  Serial.println();
}


void call(){
  // SIM module
  mySerial.begin(9600);
  Serial.println("Messege Initializing..."); 
  delay(1000);

  mySerial.println("AT"); //Once the handshake test is successful, it will back to OK
  Serial.println("Messege AT"); 
  
  updateSerial();
  mySerial.println("AT+CMGF=1"); // Configuring TEXT mode
  updateSerial();
  mySerial.println("AT+CMGS=\"+94767443330\"");//change ZZ with country code and xxxxxxxxxxx with phone number to sms
  updateSerial();
  mySerial.print("Fall Detected"); //text content
  updateSerial();
  mySerial.write(26); //can this be commented????
}

void call2(){

  mySerial.begin(9600);

  Serial.println("Initializing..."); 
  delay(1000);

  mySerial.println("AT"); //Once the handshake test is successful, i t will back to OK
  updateSerial();
  
  mySerial.println("ATD+ +94767443330;"); //  change ZZ with country code and xxxxxxxxxxx with phone number to dial
  updateSerial();
  delay(20000); // wait for 20 seconds...
  mySerial.println("ATH"); //hang up
  updateSerial();

}



void updateSerial()
{
  delay(500);
  while (Serial.available()) 
  {
    mySerial.write(Serial.read());//Forward what Serial received to Software Serial Port
  }
  while(mySerial.available()) 
  {
    Serial.write(mySerial.read());//Forward what Software Serial received to Serial Port
  }
}