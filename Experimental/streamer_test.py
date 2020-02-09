import serial
ser = serial.Serial('/dev/rfcomm2', 9600)

for i in range(50):	
	ser.write(str(i).encode())
	
ser.close()
