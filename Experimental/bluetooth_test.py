import bluetooth

print("Fuck this")

bd_addr = "C4:9D:ED:B2:EE:0E"

port = 1

sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))

sock.send("Please work bitch")

sock.close()
