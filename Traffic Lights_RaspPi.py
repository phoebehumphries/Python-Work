
GPIO_RED = 22
GPIO_AMBER = 23
GPIO_GREEN = 24
GPIO_SWITCH = 17
# time delay in secs
TIME_CHANGE = 1
TIME_RED = 5
TIME_GREEN = 5
#only req if not using switch

import RPi.GPIO as GPIO
# import time module used for sleep import time
# Use GPIO pin numbering disable in-use warnings
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# Setup relevant pins
GPIO.setup(GPIO_RED, GPIO.OUT)
GPIO.setup(GPIO_AMBER, GPIO.OUT)
GPIO.setup(GPIO_GREEN, GPIO.OUT)
GPIO.setup(GPIO_SWITCH, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# start with red light on
GPIO.output(GPIO_RED, True)
GPIO.output(GPIO_AMBER, False)
GPIO.output(GPIO_GREEN, False)
# Loop keeps running while 1: # red light on - sleep for set period of time
time.sleep (TIME_RED)
# Red and amber (puffin crossing - so don't flash)
GPIO.output (GPIO_AMBER, True)
# sleep for change time
time.sleep (TIME_CHANGE)
# Change to green
GPIO.output(GPIO_RED, False)
GPIO.output(GPIO_AMBER, False)
GPIO.output(GPIO_GREEN, True)

# loops until GPIO becomes "False" ie switch pressed
while GPIO.input(GPIO_SWITCH):
# sleep used to reduce processor usage #sleep for 1/4 sec between checking switch
    time.sleep (0.25) 
# Change to amber
GPIO.output(GPIO_AMBER, True)
GPIO.output(GPIO_GREEN, False)
# sleep for change time
time.sleep (TIME_CHANGE)
# Change to red
GPIO.output(GPIO_RED, True)
GPIO.output(GPIO_AMBER, False)
