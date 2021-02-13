import RPi.GPIO as GPIO
from time import sleep

def mr_fwd():
        GPIO.output(23, GPIO.LOW)
        #time.sleep(0.01)
        GPIO.output(24, GPIO.HIGH)
        #time.sleep(0.01)
def mr_rev():
        GPIO.output(24, GPIO.LOW)
        #time.sleep(0.01)
        GPIO.output(23, GPIO.HIGH)
        #time.sleep(0.01)
def ml_fwd():
        GPIO.output(25, GPIO.LOW)
        #time.sleep(0.01)
        GPIO.output(8, GPIO.HIGH)
        #time.sleep(0.01)
def ml_rev():
        GPIO.output(8, GPIO.LOW)
        #time.sleep(0.01)
        GPIO.output(25, GPIO.HIGH)
        #time.sleep(0.01)
def mr_stop():
        GPIO.output(23, GPIO.LOW)
        #time.sleep(0.01)
        GPIO.output(24, GPIO.LOW)
        #time.sleep(0.01)
def ml_stop():
        GPIO.output(25, GPIO.LOW)
        #time.sleep(0.01)
        GPIO.output(8, GPIO.LOW)
        #time.sleep(0.01)

# pin setup:
#GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT) # Setup Motor 1.
GPIO.setup(24, GPIO.OUT) # Setup Motor 1.
GPIO.setup(25, GPIO.OUT) # Setup Motor 2.
GPIO.setup(8, GPIO.OUT) # Setup Motor 2.
sleep(0.1)

def forward():
        print("Going Forwards")
        mr_fwd()
        ml_fwd()
        #sleep(2)

def backward():
        print("Going Backwards")
        mr_rev()
        ml_rev()
        #sleep(2)

def turnRight():
        print("Going Right")
        mr_rev()
        ml_fwd()
        #sleep(2)

def turnLeft():
        print("Going Left")
        mr_fwd()
        ml_rev()
        #sleep(2)

def stop():
        print("Stopping")
        mr_stop()
        ml_stop()
