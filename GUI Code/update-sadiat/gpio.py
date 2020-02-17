import RPi.GPIO as GPIO
from time import sleep

wrong = 22
correct = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(wrong, GPIO.OUT)
GPIO.setup(correct, GPIO.OUT)

try:

    while(True):
        GPIO.output(correct, GPIO.HIGH)
        GPIO.output(wrong, GPIO.HIGH)

except KeyboardInterrupt:
    GPIO.cleanup()