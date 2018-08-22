Baudrate: 38400
Data Bits: 7
Parity: none
Stop Bit: 1

7-N-1
------------
1.0
15 3A 4E 44 64 00 01 00 01 00 0E 00 0E 12 7F 5B
3A 00 01 00 0C 01 00 01 00 01 01 00 00 00 00 6F

2.25
15 3A 4E 44 64 00 01 00 01 00 0E 00 0E 01 7F 6C
3A 00 01 02 25 01 00 01 00 01 01 00 00 10 00 48

22.22
15 3A 4E 44 64 00 01 00 01 00 0E 00 0E 01 7F 6C
3A 00 01 02 22 20 00 01 00 01 01 00 00 10 01 2A

400.5
15 3A 4E 44 64 00 01 00 01 00 0E 00 0E 01 7F 6C
3A 00 01 04 00 50 00 01 00 01 01 00 00 10 02 19

800.975
15 3A 4E 44 64 00 01 00 01 00 0E 00 0E 01 7F 6C
3A 00 01 08 00 17 50 00 00 01 01 00 00 10 02 7E


Format:
	WILL FALLBACK TO INTEGER IF .0
	Header:
		15 3A 4E 44 64 00 01 00 01
	Data Length x2 - 2bytes:
		has to suit 4n+2 where n>0
	Middle:
		01 7F hex{{119 - (bytelength times 2) }} 3A
	String data:
		Starting in 00 01 
		Data, split between 4bits (always starts in last 4 bits of first bytes)
		
		Pad to length with 00
		10
		Number of half-bytes past first data byte
		  ie 3A 00 01 04 02 with 01 would place 40.2
	Ending byte:
		CheckSum 8 bit, +80hex,128dec if paddingbytes <= 2