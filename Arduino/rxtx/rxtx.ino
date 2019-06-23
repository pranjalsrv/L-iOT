#include <SoftwareSerial.h>

SoftwareSerial mySerial(10, 11); // RX, TX

void setup() {
  // opening serial communication for port and laptop
  Serial.begin(1200);
  delay(100);
  while (!Serial) {
    ; //waiting for serial port
  }


  //Serial.print("Start TXRX");

  // set the data rate for the SoftwareSerial port
  mySerial.begin(2400);
  delay(100);
  //mySerial.print("Hello, world?");
}

void loop() { // run over and over
  if (mySerial.available()) {
    Serial.println(mySerial.read());
  delay(100);
  }
  
  if (Serial.available()) {
    mySerial.println(Serial.read());
    delay(100);
  }
}
