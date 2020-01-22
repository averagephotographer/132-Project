import RPi.GPIO as GPIO
from time import sleep

#Setting up the LED and switch pin numbers
leds = [20, 22]
buttons = [12, 14, 26, 24]

#Use the Broadcam pin code
GPIO.setmode(GPIO.BCM)

#Setup the LED and switch pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(buttons, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

#GPIO pins
while(True):
    #light LED if answer is true
    if (GPIO.input(button) == GPIO.HIGH):
        GPIO.output(led, GPIO.HIGH)
