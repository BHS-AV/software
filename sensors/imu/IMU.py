import serial

imu_data_template = {
    "time": 0,
    "aX": 0.0,
    "aY": 0.0,
    "aZ": 0.0,
    "gX": 0.0,
    "gY": 0.0,
    "gZ": 0.0
}


class IMU:
    def __init__(self, serial_port):
        self.serial_port = serial_port
        self.imu_com = serial.Serial(serial_port, 115200, timeout=1)
        self.aX = 0
        self.aY = 0
        self.aZ = 0
        self.gX = 0
        self.gY = 0
        self.gZ = 0
        self.imu_data_old = imu_data_template.copy()
        self.imu_data = imu_data_template.copy()

    def read_raw(self):
        raw = None
        try:
            raw = self.imu_com.readline()
        except serial.SerialException:
            print("Data not Received")
        return raw

    def read_data(self):
        raw = self.read_raw()
        decoded = raw.decode("utf-8")
        decoded = decoded.replace("\r\n", "")
        split = decoded.split(', ')
        while len(split) == 0:
            raw = self.read_raw()
            decoded = raw.decode("utf-8")
            split = decoded.split(', ')
        return split

    def parse_data(self):
        self.imu_data_old = self.imu_data.copy()
        data = self.read_data()
        self.imu_data["time"] = int(data[0])
        self.imu_data["aX"] = float(data[1])
        self.imu_data["aY"] = float(data[2])
        self.imu_data["aZ"] = float(data[3])
        self.imu_data["gX"] = float(data[4])
        self.imu_data["gY"] = float(data[5])
        self.imu_data["gZ"] = float(data[6])

        return self.imu_data


if __name__ == '__main__':
    handler = IMU('COM7')
    print(handler.read_data())
