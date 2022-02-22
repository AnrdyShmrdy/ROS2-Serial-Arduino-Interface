const int genLed = 3;    // pin the yellow LED is attached to

void setup() {

  // make the LED pins outputs
  pinMode(genLed, OUTPUT);

  // start serial communication for debugging
  Serial.begin(9600);

}

void loop() {

  if(Serial.available()>0){
    command = Serial.readStringUntil("!");
    Serial.print("A command was recieved via Serial: ");
    Serial.println(command);
    if(command == "genon!"){
      digitalWrite(genLed,HIGH);
      Serial.println("gen Led is on!");
    }
    if(command == "genoff!"){
      digitalWrite(genLed,LOW);
      Serial.println("gen Led is off!");
    }
  }

  }
