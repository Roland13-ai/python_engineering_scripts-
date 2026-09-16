#include <SoftwareSerial.h>

SoftwareSerial BT(10, 11); // RX, TX du HC-05

int light1 = 7; 
int light2 = 8;
char order;

void setup() {
  pinMode(light1, OUTPUT);
  pinMode(light2, OUTPUT);
  digitalWrite(light1, LOW);
  digitalWrite(light2, LOW);
  
  BT.begin(9600);
  Serial.begin(9600);
  Serial.println("System ready");
}

void loop() {
  if (BT.available()) {
    order = BT.read();
    Serial.print("order received: ");
    Serial.println(order);
    
    if (order == '1') {
      digitalWrite(light1, HIGH); 
      BT.println("light1 ON");
    }
    if (order == '2') {
      digitalWrite(light2, HIGH); 
      BT.println("light2 ON");
    }
    if (order == '0') {
      digitalWrite(light1, LOW);
      digitalWrite(light2, LOW);
      BT.println("All OFF");
    }
  }
}

