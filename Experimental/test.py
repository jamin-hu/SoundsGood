#!/usr/bin/env python

import signal

import skywriter

positionValues = []

some_value = 5000

@skywriter.move()
def move(x, y, z):
    yArray = [0,0,0,0,0,0,0,0,0,0]
    y = int(round(z*10))
    yArray[y-1] = 1
    print( yArray)

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
