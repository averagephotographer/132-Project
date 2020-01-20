# GPIO stuff
import RPi.GPIO as GPIO


# code stolen from BinaryAddiction hw:
def setGPIO():
    # define the pins (change these if they are different)
    gpio = [12, 16, 17, 18, 20, 21, 22, 26, 27]
    # set them up as output pins
    GPIO.setup(gpio, GPIO.OUT)
    return gpio

def setNum():
    # create an empty list to represent the bits
    num = []
    # generate eight random bits
    for i in range (0, 8):
        # append a random bit (0 or 1) to the end of the list
        num.append(randint(0, 1))

    return num

def display():
    for i in range(len(sum)):
        # if the i-th bit is 1, then turn the i-th LED on
        if (sum[i] == 1):
            GPIO.output(gpio[i], GPIO.HIGH)
        # otherwise, turn it off
        else:
            GPIO.output(gpio[i], GPIO.LOW)

######
# main
######

# use the Broadcom pin scheme
GPIO.setmode(GPIO.BCM)

# setup the GPIO pins
gpio = setGPIO()

# get a random num1 and display it to the console
num1 = setNum()
print "     ", num1

# get a random num2 and display it to the console
num2 = setNum()
print "+    ", num2

# calculate teh sum of num1 + num2 and display it to the console
sum = calculate(num1, num2)
print "= ", sum

# turn on the appropriate LEDs to "display" the sum
display()

# wait for user input before cleaning up and resetting GPIO pins
raw_input("press ENTER to terminate")
GPIO.cleanup()
