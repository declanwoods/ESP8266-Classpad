import serial
from math import ceil
from functools import reduce

class Classpad(object):
	def __init__(self, port):
		self.port = port
		self.baudrate = 38400
		self.bytesize = 7
		self.serial = None
		self.stringHeader = "3A4E446400010001"

	def open(self, s=None):
		if s == None:
			s = serial.Serial(self.port, baudrate=self.baudrate, bytesize=self.bytesize)
		self.serial = s

	def close(self):
		if self.serial:
			self.serial.close()

	def writeString(self, text):
		if not self.serial:
			return False

		if len(text) > 118:
			return False

		output = ""
		output += self.stringHeader

		size = ((len(text)+2)+4) - ((len(text)+2)%4)
		print size
		output += (("0"*(4-len(str(chr(size))))) + hex(size+2)[2:]).upper()*2

		paddingLength = size - len(text)
		number = hex(size)[2:].upper()
		output += "057F%s3A" % number

		data = ''.join([hex(ord(x))[2:] for x in text]).upper() + "00"*paddingLength
		output += "0001"+data

		checksum = "7F"
		if len(text) > 0:
			checksum = reduce(lambda x,y: x+y, [int(hex(ord(x))[2:], 16) for x in text])
			checksum = hex(255-(checksum % 256))[2:].upper()

		output += checksum

		print output
		self.serial.write(output)

		return True