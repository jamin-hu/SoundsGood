
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
duration = 1   # in seconds, may be float
f = 440.0        # sine frequency, Hz, may be float



p = pyaudio.PyAudio() 

#stream = p.open(format = FORMAT, 
#                channels = CHANNELS, 
#                rate = RATE, 
#                input = True, 
#                output = True, 
#                frames_per_buffer = chunk) 



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
    
    fs = 220 + z*220
    
    print("Z = " + str(z))
    print("New Fs = " + str(fs))
    
    global stream
    
    sine = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)
    stream.write(sine)


    print(yArray)
    

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
