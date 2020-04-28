import serial

# Arduino Nano default port
PORT = "COM7"
BAUD_RATE = 9600
TIMEOUT = 5

# open communication with Arduino
arduino = serial.Serial(PORT, BAUD_RATE, timeout=TIMEOUT)

try:
  # try to control motors
  arduino.write(b's')
except e:
  print(e, "Could not communicate with Arduino")


arduino.close()