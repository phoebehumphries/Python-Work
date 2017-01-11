import RPi.GPIO as GPIO
import time

'''This is the reverse code to Anju's. So the lights go from right to left.'''

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(0,GPIO.OUT)
GPIO.setup(1,GPIO.OUT)
GPIO.setup(2,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)

GPIO.output(4,GPIO.HIGH)
#turns LED on
time.sleep(1)
#sleep for 1 sec
GPIO.output(4,GPIO.LOW)
#turns LED off

GPIO.output(3,GPIO.HIGH)
time.sleep(1)
GPIO.output(3,GPIO.LOW)

GPIO.output(2,GPIO.HIGH)
time.sleep(1)
GPIO.output(2,GPIO.LOW)

GPIO.output(1,GPIO.HIGH)
time.sleep(1)
GPIO.output(1,GPIO.LOW)

GPIO.output(0,GPIO.HIGH)
time.sleep(1)
GPIO.output(0,GPIO.LOW)


