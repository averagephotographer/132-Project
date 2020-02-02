##import RPi.GPIO as GPIO
from time import sleep

#Setting up the LED and switch pin numbers
wrong = 22
correct = 20
##button_1 = 12
buttons = [12, 16, 24, 26]
##button_2 = 16
##button_3 = 26
##button_4 = 24

#Use the Broadcam pin code
GPIO.setmode(GPIO.BCM)

#Setup the LED and switch pins
##GPIO.setmode(GPIO.BCM)
GPIO.setup(wrong, GPIO.OUT)
GPIO.setup(correct, GPIO.OUT)
GPIO.setup(buttons, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
##GPIO.setup(button_2, GPIO.OUT)
##GPIO.setup(button_3, GPIO.OUT)
##GPIO.setup(button_4, GPIO.OUT)
#####################
##ans = ["a", "b", "c", "D"]
##button_1 = ans[0]
#####################

#GPIO pins
while(True):
    #light LED if answer is true
    if (GPIO.input(buttons[0]) == GPIO.HIGH):
        GPIO.output(correct, GPIO.HIGH)
    for i in range(1,len(buttons)):
        if(GPIO.input(buttons[i]) == GPIO.HIGH):
            GPIO.output(wrong, GPIO.HIGH)
##    else:
##        GPIO.output(wrong, GPIO.HIGH)
