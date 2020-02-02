import RPi.GPIO as GPIO
from time import sleep

#Setting up the LED and switch pin numbers
wrong = 22
correct = 20
buttons = [12, 16, 24, 26]

#Use the Broadcam pin code
GPIO.setmode(GPIO.BCM)

#Setup the LED and switch pins
GPIO.setup(wrong, GPIO.OUT)
GPIO.setup(correct, GPIO.OUT)
GPIO.setup(buttons, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
#####################

#GPIO pins
try:
    while(True):
        #light LED if answer is true
        if (GPIO.input(buttons[0]) == GPIO.HIGH):
            GPIO.output(correct, GPIO.HIGH)
        for i in range(1,len(buttons)):
            if(GPIO.input(buttons[i]) == GPIO.HIGH):
                GPIO.output(wrong, GPIO.HIGH)

except KeyboardInterrupt:
    # reset the GPIO pints
    GPIO.cleanup()