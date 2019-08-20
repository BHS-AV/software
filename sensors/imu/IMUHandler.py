import serial


class IMUHandler:
    def __init__(self, serial_port):
        self.serial_port = serial_port
        self.imu_com = serial.Serial(serial_port, 115200, timeout=1)

    def read_raw(self):
        raw = self.imu_com.readline()
        return raw

    def read_data(self):
        raw = self.read_raw()
        decoded = raw.decode("utf-8")
        split = decoded.split(', ')
        while len(split) == 0:
            raw = self.read_raw()
            decoded = raw.decode("utf-8")
            split = decoded.split(', ')
        return split

    def parse_imu(self):
        return


if __name__ == '__main__':
    handler = IMUHandler('COM7')
    print(handler.read_data())
