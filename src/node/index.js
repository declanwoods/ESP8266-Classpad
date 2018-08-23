class Classpad {
	constructor(port) {
		self.port = port
		self.baudrate = 38400
		self.bytesize = 7
		self.serial = null
		self.noSerial = port==null
		self.header = "3A4E446400010001"
	}
	open(s=null) {
		if (s != null) {
			s = null;
		}
		this.serial = s;
		return true;
	}
	close() {
		if (this.serial) {
			this.serial.close();
		}
		return true;
	}
	writeString(text) {
		if !(this.serial==null) && !(self.noSerial==null) {
			return false;
		}
	}
	writeInteger(num) {
		if !(this.serial==null) && !(self.noSerial==null) {
			return false;
		}
	}
	writeFloat(num) {
		if !(this.serial==null) && !(self.noSerial==null) {
			return false;
		}

		if (Math.floor(num) == num) {
			return writeInteger(Math.floor(num));
		}
	}
}

module.exports = Classpad;