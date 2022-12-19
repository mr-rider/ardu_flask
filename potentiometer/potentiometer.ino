// potentiometer.ino
// reads a potentiometer sensor and sends the reading over serial

int sensorPin = A0; // the potentiometer is connected to analog pin 0
int ledPin = LED_BUILTIN; // the LED is connected to digital pin builtin
int sensorValue; // an integer variable to store the potentiometer reading

void setup(){
  pinMode (ledPin, OUTPUT);
  // initialize serial communication
  Serial.begin(9600);
}

void loop() {
  sensorValue = analogRead(sensorPin); // read the sensor
  Serial.println(sensorValue); // output reading to the serial line
  if (sensorValue < 20){
    digitalWrite(ledPin, LOW ); } // turn the LED off
  else {
    digitalWrite(ledPin, HIGH );} // keep the LED on
  delay (100); // Pause in milliseconds before next reading
}
  
