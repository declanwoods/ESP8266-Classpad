import casio_classpad

obj = casio_classpad.Classpad("/dev/tty.usbserial-1410")
obj.open()
print obj.writeString("test")