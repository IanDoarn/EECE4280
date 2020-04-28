// Define stepper motor connections:
// Outer motor identify:
#define dirPin_out 10
#define stepPin_out 8

// inner motor identify:
#define dirPin_in 5
#define stepPin_in 3

#define stepsPerRevolution 6400
#define pulseWidth 30 // Speed (lower is faster)
#define tDelay 5000

int val;
int height_in;
int height_out;

boolean alreadyRun = false;

void setup() {

  Serial.begin(9600);

  // Declare pins as output:
  pinMode(stepPin_out, OUTPUT);
  pinMode(dirPin_out, OUTPUT);
  pinMode(stepPin_in, OUTPUT);
  pinMode(dirPin_in, OUTPUT);
  
  // Set the spinning direction CW/CCW:
  digitalWrite(dirPin_in, HIGH);
  digitalWrite(dirPin_out, HIGH);
}

void initial_settingup(){

  // read the user input from height 0 - 4
  if (Serial.available()) {
    val = Serial.parseInt();
    Serial.println(val);

    switch (val) {
      //the camera height will be related to the user input, we will figure it out
      case 0:
        height_in = 0;
        height_out = 0;
        break;
      
      case 1:
        height_in = 70;
        height_out = 0;
        break;
        
      case 2:
        height_in = 100; 
        height_out = 0;
        break;
        
      case 3:
        height_in = 100;
        height_out = 50;
        break;
      
      case 4:
        height_in = 140;
        height_out = 100;
        break;
    }

    // Move motors to position
    
    for(int i = 0; i< height_in; i++) {
      // Set the spinning direction clockwise:
      digitalWrite(dirPin_in, LOW);

      // Spin the stepper motor 1 revolution slowly:
      for (int i = 0; i < stepsPerRevolution; i++) {
        // These four lines result in 1 step:
        digitalWrite(stepPin_in, HIGH);
        delayMicroseconds(pulseWidth);
        digitalWrite(stepPin_in, LOW);
        delayMicroseconds(pulseWidth);
      }
    }

    delay(tDelay);

    if (height_out != 0){
      for(int i = 0; i< height_out; i++) {
        // Set the spinning direction clockwise:
        digitalWrite(dirPin_out, LOW);

        // Spin the stepper motor 1 revolution slowly:
        for (int i = 0; i < stepsPerRevolution; i++) {
          // These four lines result in 1 step:
          digitalWrite(stepPin_out, HIGH);
          delayMicroseconds(pulseWidth);
          digitalWrite(stepPin_out, LOW);
          delayMicroseconds(pulseWidth);
        }
      }
    }
    delay(tDelay);
    Serial.println("camera is now positioned! Go head");
    alreadyRun = true;
  }
}

// camera position goes down
void end_system() {
  
  // Inside motor
  for(int i = 0; i< height_in; i++) {
    // Set the spinning direction clockwise:
    digitalWrite(dirPin_in, HIGH);

    // Spin the stepper motor 1 revolution slowly:
    for (int i = 0; i < stepsPerRevolution; i++) {
      // These four lines result in 1 step:
      digitalWrite(stepPin_in, HIGH);
      delayMicroseconds(pulseWidth);
      digitalWrite(stepPin_in, LOW);
      delayMicroseconds(pulseWidth);
    }
  }

  // Wait before next motor
  delay(tDelay);

  // Only change height of outside motor if it was extended
  if (height_out != 0) {
    
    // Outside motor
    for(int i = 0; i< height_out; i++) {
      // Set the spinning direction clockwise:
      digitalWrite(dirPin_out, HIGH);

      // Spin the stepper motor 1 revolution slowly:
      for (int i = 0; i < stepsPerRevolution; i++) {
        // These four lines result in 1 step:
        digitalWrite(stepPin_out, HIGH);
        delayMicroseconds(pulseWidth);
        digitalWrite(stepPin_out, LOW);
        delayMicroseconds(pulseWidth);
      }
    }
  }
  delay(tDelay);
  Serial.println("camare go back to initial position");
}

void loop() {

  // run the setup function to locate the camera
  if (!alreadyRun){
    initial_settingup();
  }
  
  // camera goes back the initial location
  if (Serial.available()) {
    char v = Serial.read();
    if (v.equals('s')){
      Serial.println("Turning off...");
      end_system();
      Serial.flush();
    }
  }
}