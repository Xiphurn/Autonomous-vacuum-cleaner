#include <Stepper.h>
#include <SoftwareSerial.h>  //header file of software serial port
SoftwareSerial Serial1(2, 3); //define software serial port name as Serial1 and define pin2 as RX and pin3 as TX
const int nbpas = 2048;
Stepper myStepper(nbpas, 8, 9, 10, 11);
float distance;  //actual distance measurements of LiDAR
float somme;
int check;  //save check value
int i;
int j =0;
bool test;
String donnees;
int uart[9];  //save data measured by LiDAR
const int HEADER = 0x59; //frame header of data package
int k;


float getdistance()  //Function that allows to get the measured distance from the LIDAR
{
  bool test;
  test = false;
  while (test!= true)
  { 
    if (Serial1.available()>0) //check if serial port has data input
    { test = true ;
      if (Serial1.read() == HEADER) //assess data package frame header 0x59
      {
        uart[0] = HEADER;
        if (Serial1.read() == HEADER) //assess data package frame header 0x59
        {
          uart[1] = HEADER;
          for (i = 2; i < 9; i++) //save data in array
          {
            uart[i] = Serial1.read(); //Reads the data from the LIDAR and saves it in a "Tableau"
          }
          check = uart[0] + uart[1] + uart[2] + uart[3] + uart[4] + uart[5] + uart[6] + uart[7];
          if (uart[8] == (check & 0xff))//verify the received data as per protocol
          {
            distance =  uart[2] + uart[3] * 256;  //calculate distance value
            
          }
        }
      }
     } 
  }
     return(distance); // Sends back the measured distance by the LIDAR
}
     


void setup()
{
  Serial.begin(115200); //set bit rate of serial port connecting Arduino with computer
  Serial1.begin(115200);  //set bit rate of serial port connecting LiDAR with Arduin
  myStepper.setSpeed(9);  //set the motor speed
}

void loop()
{
  
  j=1;
  while (j<181) //allows to send the data for each angle from 0 degrees to 180 degrees
    {
    myStepper.step(5.688); //move the stepmotor 1 degree
    somme = 0; //reset the sum value
    
    for (k=0 ; k<10 ; k++) ////adds 10 measurements to calculate the average later 
      {
        somme = somme + getdistance(); 
      }
      
    Serial.print(String(j)); //Sends the motor angle 
    Serial.print(" , "); //character that allows the data to be splitted into the Python algorithm
    Serial.println(String(somme/10)); //Sends the sum divided by the number of measurements 
    delay (10);
    j = j + 1;
    }
    
  delay(500);

  
  j=179;
  while (j>-1) //allows to send the data for each angle from 180 degrees to 0 degrees
    {
      myStepper.step(-5.688); //move the stepmotor 1 degree in the other direction 
      somme = 0; //reset the sum value
      
      for (k=0 ; k<10 ; k++) //adds 10 measurements to calculate the average later 
        {
          somme = somme + getdistance(); 
        }
        
      Serial.print(String(j)); //Sends the motor angle
      Serial.print(" , "); //character that allows the data to be splitted into the Python algorithm 
      Serial.println(String(somme/10)); //Sends the sum divided by the number of measurements
      delay (10);
      j = j - 1; 
    }
    
  delay(500);

  
}
