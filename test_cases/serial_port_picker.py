import serial.tools.list_ports

def select_Port():
    ports = serial.tools.list_ports.comports()

    print("Select a serial port: ")
    for port in ports:
        print("(" + str(ports.index(port)) + ") " + str(port))

    while True:
        try:
            selected = int(input("Chosen Port: "))
            if selected in range(len(ports)):
                break
            else:
                print("Out of range")
        except:
            print("Invalid input")

    return str(ports[selected][0])
