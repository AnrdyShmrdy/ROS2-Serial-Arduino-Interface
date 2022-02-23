const int Led = 3;    // pin the yellow LED is attached to
String command;
void setup() {

  // make the LED pins outputs
  pinMode(Led, OUTPUT);

  // start serial communication for debugging
  Serial.begin(115200);

}

void loop() {

  if(Serial.available()>0){
    command = Serial.readStringUntil("!");
    if(command == "ledon!"){
      digitalWrite(Led,HIGH);
    }
    if(command == "ledoff!"){
      digitalWrite(Led,LOW);
    }
  }

  }
