Baudrate: 38400
Data Bits: 7
Parity: none
Stop Bit: 1

7-N-1
------------
test88888828888888
15 3A 4E 44 64 00 01 00 01 00 16 00 16 05 7F 58
3A 00 01 74 65 73 74 38 38 38 38 38 38 32 38 38
38 38 38 38 38 00 22 13 

test8888882888
15 3A 4E 44 64 00 01 00 01 00 12 00 12 05 7F 60
3A 00 01 74 65 73 74 38 38 38 38 38 38 32 38 38
38 00 00 15

123456
15 3A 4E 44 64 00 01 00 01 00 0A 00 0A 05 7F 70
3A 00 01 31 32 33 34 35 36 00 00 4A

1234567
15 3A 4E 44 64 00 01 00 01 00 0A 00 0A 05 7F 70
3A 00 01 31 32 33 34 35 36 37 00 13 

12345678
15 3A 4E 44 64 00 01 00 01 00 0E 00 0E 05 7F 68
3A 00 01 31 32 33 34 35 36 37 38 00 00 00 00 5B

88888888
15 3A 4E 44 64 00 01 00 01 00 0E 00 0E 05 7F 68
3A 00 01 38 38 38 38 38 38 38 38 00 00 00 00 3F


Format:
	Header:
		15 3A 4E 44 64 00 01 00 01
	String Length x2 - 2bytes:
		has to suit 4n+2 where n>0
	Middle:
		05 7F {{78 - (bytelength-2) }} 3A
	String data:
		Starting in 00 01
		Ascii data
		Pad to length with 00
	Ending byte:
		CheckSum 8 bit , +80hex,128dec if paddingbytes <= 2

