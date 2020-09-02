import socket
import json
import base64
import time
import matplotlib.pyplot as plt
import numpy as np

localIP     = "192.168.0.10"
localPort   = 1789
bufferSize  = 1024

msgFromServer       = "Hello UDP Client"
bytesToSend         = str.encode(msgFromServer)

tvocReadings = []
co2Readings = []
temperatureReadings = []
pressureReadings = []

#plt.ion()
#fig = plt.figure()
#ax = fig.add_subplot(111)
#ax.plot(tvocReadings, label='$y TVOC readings in ppb')

#plt.ylim(0, 2)
#fig.canvas.draw()

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")

# Listen for incoming datagrams
while(True):
	bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
	message = bytesAddressPair[0]
	address = bytesAddressPair[1]

	payload = json.loads(message)
	
	localtime = time.localtime(time.time())

	# Parse sensor reading.
	packet_data = bytearray(base64.b64decode(payload["rxpk"]["data"]))

	# Deserialize packet data.
	idx = 0
	node_id = packet_data[idx] + packet_data[idx+1] * 256 + packet_data[idx+2] * 256 * 256 + \
		packet_data[idx+3] * 256 * 256 * 256
	idx += 4
	tvoc_level = packet_data[idx] + packet_data[idx+1] * 256
	idx += 2
	co2_level = packet_data[idx] + packet_data[idx+1] * 256
	idx += 2
	temperature = (packet_data[idx] / 65536.0) + (packet_data[idx+1] / 256.0) + \
	  packet_data[idx+2] + (packet_data[idx+3] * 256.0)
	idx +=4
	pressure = (packet_data[idx] / 65536.0) + (packet_data[idx+1] / 256.0) + \
	  packet_data[idx+2] + (packet_data[idx+3] * 256.0) 
	idx += 4

	print("\n")
	print("Packet received at {}.{}.{}-{}:{}:{}".format(localtime[2], localtime[1], \
		localtime[0], localtime[3], localtime[4], localtime[5]))
	print("\tGateway ID: {}".format(payload["rxpk"]["gateway-id"]))
	print("\tNode ID: {}".format(node_id))
	print("\tChannel frequency: {}".format(payload["rxpk"]["frequency"]))
	print("\tTimestamp in miliseconds: {}".format(payload["rxpk"]["timestamp"]))
	print("\tRssi: {}".format(payload["rxpk"]["rssi"]))
	print("\tTVOC level: {}ppb".format(tvoc_level))
	print("\tCO2 level: {}ppm".format(co2_level))
	print("\tTemperature: {}C".format(temperature))
	print("\tPressure: {}mbar".format(pressure))

	# Sending a reply to client
	UDPServerSocket.sendto(bytesToSend, address)

	#tvocReadings.append(float(tvoc_level))
	#ax.plot(tvocReadings, label='$y TVOC readings in ppb')
	#fig.canvas.draw()