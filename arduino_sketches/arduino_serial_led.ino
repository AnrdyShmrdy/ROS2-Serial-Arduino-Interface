const int Led = 3;

void setup() 
{
  pinMode(Led, OUTPUT);
  Serial.begin(9600);
  while (! Serial); // Wait until Serial is ready
  Serial.println("Enter 0 to turn off LED and 1 to turn on LED");
}

void loop() 
{
  if (Serial.available())
  {
    char ch = Serial.read();
    if (ch == '0')
    {
      digitalWrite(Led,LOW);
      delay(10);
      Serial.println("Led Turned OFF");
    }
    if (ch == '1')
    {
      digitalWrite(Led,HIGH);
      delay(10);
      Serial.println("Led Turned ON");
    }
  }
}