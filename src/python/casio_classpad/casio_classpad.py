import serial
from math import ceil
from functools import reduce
import binascii
from time import sleep

class Classpad(object):
	def __init__(self, port, returnData=False):
		self.port = port
		self.baudrate = 38400
		self.bytesize = 7
		self.serial = None
		self.noSerial = port==None
		self.genericHeader = "3A4E446400010001"
		self.returnData = returnData

	def open(self, s=None):
		if s == None:
			s = serial.Serial(self.port, baudrate=self.baudrate, bytesize=self.bytesize)
		self.serial = s

	def close(self):
		if self.serial:
			self.serial.close()

	def sendInitialByte(self):
		if not self.serial:
			return False

		self.serial.write([0x15])
		return True

	def waitForByte(self, byte):
		response = None
		while not response:
			if self.serial.in_waiting:
				readByte = self.serial.read(1)
				print hex(ord(readByte))
				if readByte == byte:
					return True
			sleep(0.005)

	def generateChecksum(self, data, op=True):
		checksum = ""
		if len(data) > 0:
			checksum = reduce(lambda x,y: x+y, data)
			checksum = checksum % 256
			if op:
				checksum = hex(255-(checksum))[2:].upper()
			else:
				checksum = hex(checksum)[2:].upper()
		return checksum

	def writeString(self, text):
		if not self.serial and not self.noSerial:
			return False

		if len(text) > 118:
			return False


		self.sendInitialByte()
		self.waitForByte(0x16)

		header = ""
		header += self.genericHeader

		size = ((len(text))+4) - ((len(text))%4)
		header += (("0"*(4-len(str(chr(size))))) + hex(size+2)[2:]).upper()*2

		paddingLength = size - len(text)
		number = hex(128-size*2)[2:].upper()
		header += "057F%s" % number

		print header
		dataHeader = [ord(x) for x in binascii.unhexlify(header)]
		if not self.noSerial:
			self.serial.write(dataHeader)
		self.waitForByte(0x06)

		dataHex = "3A"
		dataLength = ''.join([hex(ord(x))[2:] for x in text]).upper() + "00"*paddingLength
		dataHex += "0001"+dataLength

		checksum = "7F"
		if len(text) > 0:
			checksum = self.generateChecksum([int(hex(ord(x))[2:], 16) for x in text])

		dataHex += checksum

		print dataHex
		dataBody = [ord(x) for x in binascii.unhexlify(dataHex)]
		if not self.noSerial:
			self.serial.write(dataBody)
		self.waitForByte(0x06)
		return [header, dataHex] if not self.returnData else [dataHeader, dataBody]

	def writeInteger(self, num):
		if not self.serial:
			return False

		header = ""
		header += self.genericHeader

		length = len(hex(num)[2:])  
		lengthString = "0"*(4-length) + hex(num)[2:]
		print lengthString

		header += lengthString*2
		number = hex(128-(size*2 + 8))[2:].upper()
		header += "127F%s" % number

		dataBodyLength

		print output
		data = [ord(x) for x in binascii.unhexlify(output)]
		if not self.noSerial:
			self.serial.write(data)

		return output if not self.returnData else data

	def writeFloat(self, num):
		if not self.serial: 
			return False

		if num == int(num):
			return writeInteger(int(num))

		output = ""
		output += self.genericHeader

		numberWhole = int(num//1.0)
		decimal = num - numberWhole

		print output
		data = [ord(x) for x in binascii.unhexlify(output)]
		if not self.noSerial:
			self.serial.write(data)

		return output if not self.returnData else data

	def readString(self, serialData):
		return False

	def readInteger(self, serialData):
		return False

	def readFloat(self, serialData):
		return False