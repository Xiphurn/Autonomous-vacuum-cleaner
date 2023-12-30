#include <SoftwareSerial.h>
SoftwareSerial Serial1(2, 3); // RX, TX

int uart[9];
const int HEADER = 0x59;
float lastValidDistance = -1;
unsigned long lastReadTime = 0;
const unsigned long timeout = 100; // Timeout en millisecondes

void setup() {
    Serial.begin(9600);
    Serial1.begin(115200);
}

float getDistance() {
    static int index = 0;
    static bool headerReceived = false;
    unsigned long startTime = millis();

    while (millis() - startTime < timeout) {
        if (Serial1.available()) {
            int dataByte = Serial1.read();

            if (!headerReceived) {
                if (index == 0 && dataByte == HEADER) {
                    uart[index++] = dataByte;
                } else if (index == 1 && dataByte == HEADER) {
                    uart[index++] = dataByte;
                    headerReceived = true;
                }
            } else {
                uart[index++] = dataByte;

                if (index == 9) {
                    index = 0;
                    headerReceived = false;

                    int checkSum = 0;
                    for (int i = 0; i < 8; i++) {
                        checkSum += uart[i];
                    }

                    if (uart[8] == (checkSum & 0xff)) {
                        lastValidDistance = (uart[2] + uart[3] * 256)+2;
                        lastReadTime = millis();
                        return lastValidDistance;
                    }
                }
            }
        }
    }

    if (millis() - lastReadTime > timeout) {
        return -1; // Indicateur d'erreur si la dernière lecture est trop ancienne
    }

    return lastValidDistance;
}

void loop() {
    float distance = getDistance();

    if (distance >= 0) {
        Serial.print("Distance = ");
        Serial.print(distance);
        Serial.print('\t');
        Serial.print('\n');
    } else {
        // Gérer l'erreur ici
        Serial.println("Erreur : Donnée de distance peut-être obsolète");
    }
}
