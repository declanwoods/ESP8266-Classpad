import casio_classpad

obj = casio_classpad.Classpad("/dev/tty.usbserial-1410")
obj.open()

assert obj.writeString("12345678") == "3A 4E 44 64 00 01 00 01 00 0E 00 0E 05 7F 68 3A 00 01 31 32 33 34 35 36 37 38 00 00 00 00 5B".replace(" ", "")

assert obj.writeInteger(1) == "3A 4E 44 64 00 01 00 01 00 0E 00 0E 12 7F 5B 3A 00 01 00 0C 01 00 01 00 01 01 00 00 00 00 6F".replace(" ", "")
assert obj.writeInteger(2) == "3A 4E 44 64 00 01 00 01 00 0E 00 0E 12 7F 5B 3A 00 01 00 0C 01 00 01 00 01 02 00 00 00 00 6E".replace(" ", "")
assert obj.writeInteger(22) == "3A 4E 44 64 00 01 00 01 00 0E 00 0E 12 7F 5B 3A 00 01 00 0C 01 00 01 00 01 16 00 00 00 00 5A".replace(" ", "")
assert obj.writeInteger(400) == "3A 4E 44 64 00 01 00 01 00 12 00 12 12 7F 53 3A 00 01 00 10 01 00 02 00 02 10 01 00 00 00 00 00 00 00 59".replace(" ", "")
assert obj.writeInteger(800) == "3A 4E 44 64 00 01 00 01 00 12 00 12 12 7F 53 3A 00 01 00 10 01 00 02 00 02 20 03 00 00 00 00 00 00 00 47".replace(" ", "")
