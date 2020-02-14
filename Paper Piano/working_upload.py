##################################
# Name: Andres Torres, Sadiat Ibrahim, Christopher Tullier
# Date: 2/6/2020
# Description: Paper Piano
##################################
import RPi.GPIO as GPIO
from time import sleep, time
import pygame
from array import array
from math import sin, pi

# the waveform fn is also commented out in the code
# from waveform_vis import WaveformVis


MIXER_FREQ = 44100
MIXER_SIZE = -16
MIXER_CHANS  = 1
MIXER_BUFF = 1024

# the note generator class
class Note(pygame.mixer.Sound):
    # note that volume rnages from 0.0 to 1.0
    def __init__(self, frequency, volume, waveform_name):
        self.frequency = frequency
        self.waveform_name = waveform_name
        # initialize the note using an array of samples
        pygame.mixer.Sound.__init__(self, buffer=self.build_samples(waveform_name))
        self.set_volume(volume)

    # builds an array of samples for the curent note
    def build_samples(self, waveform_name):
        # calculate teh period and amplitude of the note's wave
        period = int(round(MIXER_FREQ / self.frequency))
        amplitude = 2 ** (abs(MIXER_SIZE) - 1) - 1
        
        # initialize the note's sampels (using an array of signed 16-bit "shorts")
        samples = array("h", [0] * period)

        # generate the note's samples
        for t in range(period):
            if waveform_name == "square":
                if (t < period / 2):
                    samples[t] = amplitude
                else:
                    samples[t] = -amplitude
        
            if waveform_name == "sawtooth":
                if (t < period / 2):
                    samples[t] = (amplitude * t) / period
                else:
                    samples[t] = (amplitude * t) / period - amplitude
            
            if waveform_name == "triangle":
                if (t < period / 4):
                    samples[t] = (amplitude * t) / period
                elif (t < period / 2):
                    samples[t] = (amplitude * -t) / period + (amplitude / 2)
                elif (t <  (3 * period) / 4):
                    samples[t] = (-amplitude * t) / period + (amplitude / 2)
                else:
                    samples[t] = (amplitude * t) / period - amplitude
            
            if waveform_name == "sin":
                samples[t] = int(amplitude * (sin(((2 * pi)/period)* t)))

        # vis = WaveformVis()
        # vis.visSamples(samples, waveform_name)
        return samples

# waits until a note is pressed
def wait_for_note_start():
    while (True):
        # first, check for notes
        for key in range(len(keys)):
            if (GPIO.input(keys[key])):
                return key
        # next, check for the play button
        if (GPIO.input(play)):
            # debounce the switch
            while (GPIO.input(play)):
                sleep(0.01)
            return "play"
        # finally, check for the record button
        if (GPIO.input(record)):
            # debounce the switch
            while (GPIO.input(record)):
                sleep(0.01)
            return "record"
        sleep(0.01)

    # waits until a note is released
def wait_for_note_stop(key):
    while (GPIO.input(key)):
        sleep(0.1)

def play_song():
    # each element in the song is a lsit composed of
    # two parts: a note (or silece) and a duration
    for part in song:
        note, duration = part
        # if it's a silece, delay for its duration
        if (note == "SILENCE"):
            sleep(duration)
        # otherwise, play the note for its duration
        else:
            notes[note].play(-1)
            sleep(duration)
            notes[note].stop()
# perset mixer initialization arguments: frequency (44.1K), size
# (16 bits signed), channels (mono), and buffer size (1KB)
# then, initialize the pygame ilbrary
pygame.mixer.pre_init(MIXER_FREQ, MIXER_SIZE, MIXER_CHANS, MIXER_BUFF)
pygame.init()

# use the Broadcom pin mode
GPIO.setmode(GPIO.BCM)

# setup the pin and frequency for a C note
keys = [ 20, 16, 12, 26 ]
freqs = [261.6, 261.6, 261.6, 261.6]
waves = ["square", "sawtooth", "triangle", "sin"]
notes = []

# setup button pins
play = 19
record = 21

# setup LED pins
red = 17
green = 18
blue = 27 # if the red is too dim, use blue

# setup the input pin
GPIO.setup(keys, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(play, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(record, GPIO.IN, GPIO.PUD_DOWN)

# setup the output pins
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

# create the actual C note
for n in range(len(freqs)):
    notes.append(Note(freqs[n], 1, waves[n]))

# begin in a non-recording state and initialize teh song recording
recording = False
song = []

# the main part of the program
print ("Welcome to the paper piano")
print ("Press Ctrl_C to exit...")

# detect when Ctrl+C is pressed so that we can rest teh GPIO pins
try:
    while (True):
        # start a timer
        start = time()
        # play a note when pressed - until released
        # also detect play/record
        key = wait_for_note_start()
        # note the duration of the silece
        duration = time() - start
        # if recording, append the duration of the silence
        if (recording):
            song.append(["SILENCE", duration])
        # if teh record button was pressed
        if (key == "record"):
            # if not prevously recording, reset the song
            recording = not recording
            GPIO.output(red, recording)
        # if the play button was pressed
        elif (key == "play"):
            # if recording, stop
            if (recording):
                recording = False
                GPIO.output(red, False)
            # turn on the green LED
            GPIO.output(green, True)
            # play the song
            play_song()
            GPIO.output(green, False)
        # otherwise, a piano key was pressed
        else:
            # start the timer and play the note
            start = time()
            notes[key].play(-1)
            wait_for_note_stop(keys[key])
            notes[key].stop()
            # once the note is released, stop the timer
            duration = time() - start
            # if recording, append the note and its duration
            if (recording):
                song.append([key, duration])

except KeyboardInterrupt:
    # reset the GPIO pints
    GPIO.cleanup()
