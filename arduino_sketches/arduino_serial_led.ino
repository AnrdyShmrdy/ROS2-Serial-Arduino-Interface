const int Led = 3;    // pin the yellow LED is attached to
String command;
void setup() {

  // make the LED pins outputs
  pinMode(Led, OUTPUT);

  // start serial communication for debugging
  Serial.begin(9600);

}

void loop() {

  if(Serial.available()>0){
    command = Serial.readStringUntil("!");
    Serial.print("A command was recieved via Serial: ");
    Serial.println(command);
    if(command == "ledon!"){
      digitalWrite(Led,HIGH);
      Serial.println("Led is on!");
    }
    if(command == "ledoff!"){
      digitalWrite(Led,LOW);
      Serial.println("Led is off!");
    }
  }

  }
