void setup(){
 
Serial.begin(9600);
 
}
 
void loop(){
 
Serial.print("Water level Sensor Value:");
Serial.println(analogRead(A0));
delay(10000);
 
}
