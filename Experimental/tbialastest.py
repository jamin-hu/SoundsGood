
#!/usr/bin/env python

import signal
#import test2
import skywriter
import pyaudio 
import numpy as np 
import wave 


FORMAT = pyaudio.paInt16 
CHANNELS = 1 
RATE = 8800 
K=0 
DISTORTION = 0.61

volume = 0.5     # range [0.0, 1.0]
fs = 44100       # sampling rate, Hz, must be integer
duration = 100000*2*np.pi*1/44100   # in seconds, may be float
f = 440.0        # sine frequency, Hz, may be float
chunk = int(duration*fs)


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
                input = False,
                output=True, output_device_index=2,
                frames_per_buffer = chunk)


print("Eng Eder de Souza - ederwander")
print("Primitive Pedal")





#@skywriter.move()
#def move(x, y, z):
#    global f
#    yArray = [0,0,0,0,0,0,0,0,0,0]
#    y = int(round(z*10))
#    yArray[y-1] = 1
#    
#    f = 880 - z*440
    
    #print("Z = " + str(z))
    #print("New Fs = " + str(fs))
    
    #global stream
    
    #sine = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)
    #stream.write(sine)


    #print(yArray)
    

#@skywriter.flick()
#def flick(start,finish):
#    print('Got a flick!', start, finish)
#
#@skywriter.airwheel()
#def spinny(delta):
#    global some_value
#    some_value += delta
#    if some_value < 0:
#        some_value = 0
#    if some_value > 10000:
#        some_value = 10000
#    print('Airwheel:', some_value/100)

#@skywriter.double_tap()
#def doubletap(position):
#    print('Double tap!', position)

#@skywriter.tap()
#def tap(position):
#    print('Tap!', position)

#@skywriter.touch()
#def touch(position):
#    print('Touch!', position)


while (True):
	positionValues = []

	some_value = 5000

	sine = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32).tobytes()
	stream.write(sine)

#signal.pause()
