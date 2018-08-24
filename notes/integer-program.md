Baudrate: 38400
Data Bits: 7
Parity: none
Stop Bit: 1

7-N-1
------------
1
15 3A 4E 44 64 00 01 00 01 00 0E 00 0E 12 7F 5B
3A 00 01 00 0C 01 00 01 00 01 01 00 00 00 00 6F

2
15 3A 4E 44 64 00 01 00 01 00 0E 00 0E 12 7F 5B
3A 00 01 00 0C 01 00 01 00 01 02 00 00 00 00 6E

22
15 3A 4E 44 64 00 01 00 01 00 0E 00 0E 12 7F 5B
3A 00 01 00 0C 01 00 01 00 01 16 00 00 00 00 5A

400
15 3A 4E 44 64 00 01 00 01 00 12 00 12 12 7F 53
3A 00 01 00 10 01 00 02 00 02 10 01 00 00 00 00
00 00 00 59

800
15 3A 4E 44 64 00 01 00 01 00 12 00 12 12 7F 53
3A 00 01 00 10 01 00 02 00 02 20 03 00 00 00 00
00 00 00 47


 00 0E 00 0E 12 7F 5B
3A 00 01 00 0C 01 00 01 00 01 16 00 00 00 00 5A

Format:
	Header:
		15 3A 4E 44 64 00 01 00 01
	Data Length x2 - 2bytes:
		has to suit 4n+2 where n>0
	Middle:
		12 7F hex{{119 - (bytelength times 2) }} 3A
	String data:
		Starting in 00 01 00 10 01
		number of bytes for number x2 (2 bytes each, 4 total)
		Hex encoded integer (byte sized)
		Pad to length with 00
	Ending byte:
		CheckSum 8 bit, +80hex,128dec if paddingbytes <= 2