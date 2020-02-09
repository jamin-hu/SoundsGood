#ederwander
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
duration = 0.1   # in seconds, may be float
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


while(True): 

    #data = stream.read(chunk) 
    #data = np.fromstring(data, dtype=np.int16)  
    
    #M = 2*DISTORTION/(1-DISTORTION);
    
    #data = (1+M)*(data)/(1+K*abs(data));
    #data = np.array(data, dtype='int16') 
    #signal = wave.struct.pack("%dh"%(len(data)), *list(data))
    
    signal = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)
    
    stream.write(signal) 

stream.stop_stream() 
stream.close() 
p.terminate() 
