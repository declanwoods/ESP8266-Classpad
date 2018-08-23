import serial
import datetime

s = serial.Serial("/dev/tty.usbserial-1410", baudrate=38400, bytesize=7)

while True:
	if s.in_waiting:
		byte = s.read(1)
		string = str(hex(ord(byte)))[2:]
		string = string if len(string) == 2 else "0"+string
		print str(datetime.datetime.now()) + " - " + string.upper()
