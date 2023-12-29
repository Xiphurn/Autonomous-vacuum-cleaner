#include <Stepper.h>
#include <SoftwareSerial.h>  

SoftwareSerial Serial1(2, 3); // RX on pin 2, TX on pin 3
const int STEPS_PER_REVOLUTION = 2048;
Stepper myStepper(STEPS_PER_REVOLUTION, 8, 9, 10, 11);
const int HEADER = 0x59;  
const int BUTTON_PIN = 4; 
const unsigned long TIMEOUT = 100; // Timeout in milliseconds
float lastValidDistance = -1;
unsigned long lastReadTime = 0;
int uart[9];  

// Function to read distance from LiDAR
float getDistance() {
    static int index = 0;
    static bool headerReceived = false;
    unsigned long startTime = millis();

    while (millis() - startTime < TIMEOUT) {
        if (Serial1.available()) {
            int dataByte = Serial1.read();

            // Process header bytes
            if (!headerReceived) {
                if (index == 0 && dataByte == HEADER) {
                    uart[index++] = dataByte;
                } else if (index == 1 && dataByte == HEADER) {
                    uart[index++] = dataByte;
                    headerReceived = true;
                }
            } else { // Process data bytes
                uart[index++] = dataByte;

                if (index == 9) { // Full packet received
                    index = 0;
                    headerReceived = false;

                    int checkSum = 0;
                    for (int i = 0; i < 8; i++) {
                        checkSum += uart[i];
                    }

                    // Validate checksum
                    if (uart[8] == (checkSum & 0xff)) {
                        lastValidDistance = (uart[2] + uart[3] * 256) + 2;
                        lastReadTime = millis();
                        return lastValidDistance;
                    }
                }
            }
        }
    }

    // Error handling for timeout
    if (millis() - lastReadTime > TIMEOUT) {
        return -1; // Error if last reading is too old
    }

    return lastValidDistance;
}

void setup() {
  Serial.begin(9600);   
  Serial1.begin(115200); 
  myStepper.setSpeed(9);  
  pinMode(BUTTON_PIN, INPUT_PULLUP);  
}

void loop() {
  // Reset angle to 0 degrees when button is pushed
  while (digitalRead(BUTTON_PIN) != LOW) {  
    myStepper.step(-6); 
  }  
  int angle = 0;  
  
  // Send data for each angle from 0 to 179 degrees
  while (angle < 180) {
    myStepper.step(6);  
    float sum = 0;  
    
    for (int i = 0; i < 2; i++) {  
      sum += getDistance(); 
    }
    
    Serial.print(String(angle)); 
    Serial.print(" , ");  
    Serial.println(String(sum / 2));  

    angle++;
  }
    
  // Send data for each angle from 180 to 1 degrees
  while (angle > 0) {
    myStepper.step(-6); 
    float sum = 0; 
    
    for (int i = 0; i < 2; i++) { 
      sum += getDistance(); 
    }
    
    Serial.print(String(angle)); 
    Serial.print(" , ");  
    Serial.println(String(sum / 2)); 

    angle--; 
  }
}