#!/usr/bin/env python

import signal
#import test2
import skywriter
import serial

print("Klingt gut")
print("Voice synth")

# Setup voice
ser = serial.Serial('/dev/rfcomm2', 9600)

@skywriter.move()
def move(x, y, z):
    # print("Z = " + str(z))
    # print("New Fs = " + str(fs))
    
    global ser
    
    data_stream = (str(x) + ' ' + str(y) + ' ' + str(z) + '\n').encode()
    
    ser.write(data_stream)
    

@skywriter.flick()
def flick(start,finish):
    print('Got a flick!', start, finish)

@skywriter.airwheel()
def spinny(delta):
    global some_value
    some_value += delta
    if some_value < 0:
        some_value = 0
    if some_value > 10000:
        some_value = 10000
    print('Airwheel:', some_value/100)

@skywriter.double_tap()
def doubletap(position):
    print('Double tap!', position)

@skywriter.tap()
def tap(position):
    print('Tap!', position)

@skywriter.touch()
def touch(position):
    print('Touch!', position)

signal.pause()
