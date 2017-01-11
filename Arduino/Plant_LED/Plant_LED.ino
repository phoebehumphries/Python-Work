
int LED = 2;
int rod = 1;
int sensor = 0;

void setup() {
Serial.begin(9600);
pinMode (LED, OUTPUT);
pinMode (rod, OUTPUT);
}

void loop() {
digitalWrite(rod, HIGH);
delay(1000)
int sensorreading = analogRead(sensor);
Serial.printIn(sensorreading);

if(sensorreading >= 500)
{
  digitalWrite(LED, LOW);
}
else if (sensorreading >= 1000)
 {
  digitalWrite(LED, HIGH);
 }
digitalWrite(rod, LOW);
delay(900000);
 
