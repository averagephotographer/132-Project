##################################
# Name: Christopher Tullier
# Date: 1/29/2020
# Description: Paper Piano
##################################
# import RPi.GPIO as GPIO
from time import sleep, time
# import pygame
from array import array
from waveform_vis import WaveformVis
from math import pi, sin
DEBUG = True

MIXER_FREQ = 44100
MIXER_SIZE = -16
MIXER_CHANS  = 1
MIXER_BUFF = 1024
frequency = 261.6
# builds an array of samples for the curent note
def build_samples():
    
    # calculate the period and amplitude of the note's wave
    period = int(round(MIXER_FREQ / frequency))
    amplitude = 2 ** (abs(MIXER_SIZE) - 1) - 1
    # initialize the note's sampels (using an array of signed 16-bit 'shorts")
    samples = array("h", [0] * period)

    if DEBUG == True: 
        print "Period: {}, Amp: {}, Smpls: {}".format(period, amplitude, samples) 

    #generate the note's samples
    print "period: {}\namplitude: {}\nsamples: {}".format(period, amplitude, samples)

    
    # this is the sawtooth wave
    for t in range(period):
        if name == "sawtooth"            
            if (t < period / 2):
                # samples[t] = ((2 * amplitude) / period) * t
                samples[t] = (amplitude * t) / period

            else:
                samples[t] = (amplitude * t) / period - amplitude
       
        if name == "sin"
            samples[t] = int(amplitude * (sin(((2 * pi)/period)* t)))
        
    vis = WaveformVis()
    vis.visSamples(samples, "waveform_name")
    return samples

build_samples()
