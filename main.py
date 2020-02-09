
#!/usr/bin/env python

import signal
#import test2
import skywriter
import pyaudio
import numpy as np
import wave

chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 8800
K=0
DISTORTION = 0.61

volume = 0.5     # range [0.0, 1.0]
fs = 44100       # sampling rate, Hz, must be integer
f = 440.0        # sine frequency, Hz, may be float
duration = 40*1/f

p = pyaudio.PyAudio()

stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=fs,
                output=True)

print("Eng Eder de Souza - ederwander")
print("Primitive Pedal")

positionValues = []

some_value = 5000

sine = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)
stream.write(sine)

@skywriter.move()
def move(x, y, z):
    yArray = [0,0,0,0,0,0,0,0,0,0]
    y = int(round(z*10))
    yArray[y-1] = 1

    f = 440 + 2*z*440
    duration = 40*1/f

    print("f:", f, "duration:", duration)

    print("Z = " + str(z))

    global stream

    sine = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)
    stream.write(sine)


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
